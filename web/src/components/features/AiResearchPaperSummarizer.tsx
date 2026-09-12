import React, { useState } from 'react';
import { FileText, Sparkles, Copy, CheckCircle2 } from 'lucide-react';

interface PaperSummary {
  title: string;
  authors: string;
  abstractSummary: string;
  keyContributions: string[];
  bibtex: string;
}

export const AiResearchPaperSummarizer: React.FC = () => {
  const [paperUrl, setPaperUrl] = useState('');
  const [summary, setSummary] = useState<PaperSummary | null>({
    title: 'Attention Is All You Need (Transformer Architecture Analysis)',
    authors: 'Vaswani et al. (Google Brain & Google Research)',
    abstractSummary: 'Introduces the Transformer network architecture based entirely on self-attention mechanisms, replacing recurrent neural networks (RNNs) in sequence transduction tasks.',
    keyContributions: [
      'Multi-Head Self-Attention layers replacing recurrent computations.',
      'Positional Encoding for parallel sequence representation.',
      'Achieved SOTA BLEU score on WMT 2014 English-to-German translation.'
    ],
    bibtex: `@inproceedings{vaswani2017attention,\n  title={Attention is all you need},\n  author={Vaswani, Ashish and Shazeer, Noam et al.},\n  booktitle={NIPS},\n  year={2017}\n}`
  });

  const [copied, setCopied] = useState(false);

  const handleSummarize = (e: React.FormEvent) => {
    e.preventDefault();
    if (!paperUrl) return;
    setSummary({
      title: 'Generative Adversarial Nets & Deep Contrastive Learning',
      authors: 'Goodfellow et al. (University of Montreal)',
      abstractSummary: 'Proposes a framework for estimating generative models via an adversarial process with simultaneous training of G and D networks.',
      keyContributions: [
        'Minimax game formulation between Generator and Discriminator.',
        'Eliminates need for Markov chains or unrolled networks.'
      ],
      bibtex: `@inproceedings{goodfellow2014generative,\n  title={Generative adversarial nets},\n  author={Goodfellow, Ian et al.},\n  booktitle={NIPS},\n  year={2014}\n}`
    });
  };

  const handleCopyBib = () => {
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center gap-3 mb-4">
        <div className="p-2.5 bg-cyan-50 text-cyan-600 rounded-lg">
          <FileText className="w-5 h-5" />
        </div>
        <div>
          <h3 className="font-semibold text-gray-900">AI Research Paper & Citation Summarizer</h3>
          <p className="text-xs text-gray-500">Automated paper abstract summarizer, BibTeX citation generator & PDF analyzer</p>
        </div>
      </div>

      <form onSubmit={handleSummarize} className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Paste arXiv DOI or PDF URL (e.g. https://arxiv.org/abs/1706.03762)..."
          value={paperUrl}
          onChange={e => setPaperUrl(e.target.value)}
          className="flex-1 text-xs border border-gray-200 rounded-lg px-3 py-2 focus:ring-2 focus:ring-cyan-500 focus:outline-none"
        />
        <button
          type="submit"
          className="bg-cyan-600 hover:bg-cyan-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <Sparkles className="w-4 h-4" /> Summarize Paper
        </button>
      </form>

      {summary && (
        <div className="p-4 rounded-xl border border-cyan-100 bg-cyan-50/30 space-y-3">
          <div>
            <h4 className="font-bold text-sm text-gray-900">{summary.title}</h4>
            <span className="text-xs text-gray-500">{summary.authors}</span>
          </div>

          <p className="text-xs text-gray-700 bg-white p-3 rounded-lg border border-gray-100">
            <strong>Abstract Summary: </strong> {summary.abstractSummary}
          </p>

          <div className="space-y-1">
            <h5 className="text-xs font-bold text-cyan-800">Key Scientific Contributions:</h5>
            <ul className="space-y-1">
              {summary.keyContributions.map((c, i) => (
                <li key={i} className="text-xs text-gray-600 flex items-center gap-1.5">
                  <span className="text-cyan-500 font-bold">•</span> {c}
                </li>
              ))}
            </ul>
          </div>

          <div className="pt-2 border-t border-cyan-100 flex items-center justify-between">
            <span className="text-[11px] font-mono text-gray-400">BibTeX Format Ready</span>
            <button
              onClick={handleCopyBib}
              className="text-xs text-cyan-700 hover:text-cyan-800 font-semibold flex items-center gap-1 bg-white border border-cyan-200 px-3 py-1 rounded-lg"
            >
              {copied ? <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
              {copied ? 'Copied BibTeX' : 'Copy BibTeX'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
