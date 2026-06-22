import { Atom, ChevronRight } from "lucide-react";
import type { StudentLearningPageResponse } from "../../api";
import { MobileEmptyState } from "../../mobile/primitives";
import { periodicAreaByAreaId, profileAreaId, type AreaId } from "../periodic-table/periodicHelpers";
import { formatChapterEntryTitle } from "./learningFormat";

type LearningProfileSummary = StudentLearningPageResponse["profiles"][number];

export function LearningAreaChapterList({
  selectedArea,
  profiles,
  recommendedProfileId,
  onSelectProfile,
}: {
  selectedArea: AreaId;
  profiles: LearningProfileSummary[];
  recommendedProfileId: string;
  onSelectProfile: (profile: LearningProfileSummary) => void;
}) {
  const selectedAreaProfiles = profiles.filter((profile) => profileAreaId(profile) === selectedArea);

  return (
    <section className="chapter-card-panel" aria-label="可学习章节">
      <div className="point-list-head">
        <div>
          <p>当前选区</p>
          <h2>{periodicAreaByAreaId[selectedArea]}</h2>
        </div>
        <span>{selectedAreaProfiles.length} 个</span>
      </div>
      {selectedAreaProfiles.length ? (
        <div className="chapter-card-list">
          {selectedAreaProfiles.map((profile) => {
            const isRecommended = profile.profile_id === recommendedProfileId;
            const chapterEntryTitle = formatChapterEntryTitle(profile);
            return (
              <button
                aria-label={`${chapterEntryTitle}${isRecommended ? "，推荐学习" : ""}`}
                className={isRecommended ? "chapter-entry-card recommended" : "chapter-entry-card"}
                key={profile.profile_id}
                type="button"
                onClick={() => onSelectProfile(profile)}
              >
                <div className="chapter-entry-title">
                  <strong>{chapterEntryTitle}</strong>
                </div>
                {isRecommended ? <em>推荐学习</em> : null}
                <span className="chapter-entry-elements">{profile.element_symbols.join(" ") || profile.family_name}</span>
                <ChevronRight size={17} />
              </button>
            );
          })}
        </div>
      ) : (
        <MobileEmptyState className="empty-learning-card" icon={<Atom size={20} />}>
          <span>暂无可学习章节</span>
        </MobileEmptyState>
      )}
    </section>
  );
}
