import React from "react";

export interface PublicationItem {
  id: string;
  title: string;
  journal_conference: string;
  doi?: string;
  publication_date: string;
  citation_count: number;
  impact_factor?: number;
  is_peer_reviewed: boolean;
}

interface ResearchPublicationsListProps {
  publications: PublicationItem[];
  onAddPublicationClick?: () => void;
}

export const ResearchPublicationsList: React.FC<ResearchPublicationsListProps> = ({
  publications,
  onAddPublicationClick,
}) => {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Research & Scholarly Publications</h3>
          <p className="text-sm text-slate-400">Indexed academic journals, proceedings, and citation metrics.</p>
        </div>
        {onAddPublicationClick && (
          <button
            onClick={onAddPublicationClick}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg transition-colors"
          >
            + Index Publication
          </button>
        )}
      </div>

      <div className="space-y-4">
        {publications.length === 0 ? (
          <div className="text-center py-8 text-slate-500">No indexed research publications found.</div>
        ) : (
          publications.map((pub) => (
            <div
              key={pub.id}
              className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg hover:border-slate-600 transition-colors flex flex-col md:flex-row md:items-center justify-between gap-4"
            >
              <div className="space-y-1">
                <div className="flex items-center space-x-2">
                  <h4 className="text-base font-semibold text-slate-100">{pub.title}</h4>
                  {pub.is_peer_reviewed && (
                    <span className="px-2 py-0.5 text-[10px] uppercase tracking-wider font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded">
                      Peer Reviewed
                    </span>
                  )}
                </div>
                <p className="text-xs text-slate-400">
                  Published in <span className="text-slate-200 font-medium">{pub.journal_conference}</span> • {new Date(pub.publication_date).toLocaleDateString()}
                </p>
                {pub.doi && (
                  <p className="text-xs font-mono text-indigo-400">DOI: {pub.doi}</p>
                )}
              </div>

              <div className="flex items-center space-x-6 text-xs border-t md:border-t-0 pt-2 md:pt-0 border-slate-800">
                <div className="text-center">
                  <span className="block text-slate-400 uppercase text-[10px]">Citations</span>
                  <span className="font-mono text-base font-bold text-slate-100">{pub.citation_count}</span>
                </div>
                {pub.impact_factor !== undefined && (
                  <div className="text-center">
                    <span className="block text-slate-400 uppercase text-[10px]">Impact Factor</span>
                    <span className="font-mono text-base font-bold text-indigo-400">{pub.impact_factor.toFixed(2)}</span>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
