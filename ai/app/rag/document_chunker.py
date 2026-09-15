import re
from typing import List, Dict, Any


class DocumentChunker:
    """
    Hierarchical markdown & text document chunker with sliding windows and overlap.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_by_headers(self, text: str) -> List[Dict[str, Any]]:
        """Split text by Markdown headers (#, ##, ###) while preserving section hierarchy."""
        sections = []
        lines = text.split("\n")
        current_section = "Overview"
        current_buffer = []

        for line in lines:
            if line.startswith("#"):
                if current_buffer:
                    sections.append({
                        "section": current_section,
                        "content": "\n".join(current_buffer).strip()
                    })
                    current_buffer = []
                current_section = line.lstrip("#").strip()
            else:
                current_buffer.append(line)

        if current_buffer:
            sections.append({
                "section": current_section,
                "content": "\n".join(current_buffer).strip()
            })

        return sections

    def chunk_text(self, text: str, document_id: str) -> List[Dict[str, Any]]:
        """Chunk text with sliding window and token overlap."""
        sections = self.split_by_headers(text)
        chunks = []
        global_idx = 0

        for sec in sections:
            sec_text = sec["content"]
            words = sec_text.split()

            if not words:
                continue

            start = 0
            while start < len(words):
                end = min(start + self.chunk_size, len(words))
                chunk_words = words[start:end]
                chunk_str = " ".join(chunk_words)

                chunks.append({
                    "chunk_id": f"{document_id}_chk_{global_idx}",
                    "document_id": document_id,
                    "section": sec["section"],
                    "content": chunk_str,
                    "chunk_index": global_idx,
                    "word_count": len(chunk_words),
                })

                global_idx += 1
                start += (self.chunk_size - self.overlap)
                if end == len(words):
                    break

        return chunks
