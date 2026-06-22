import { useEffect, useMemo, useState } from "react";
import { FlaskConical, LoaderCircle } from "lucide-react";
import { StudentLearningPageResponse, errorMessage, getStudentLearningPage } from "../../api";
import { LearningState } from "../../shared/mobile/LearningState";
import { PeriodicTable } from "../periodic-table/PeriodicTable";
import { profileAreaId, type AreaId } from "../periodic-table/periodicHelpers";
import { formatRecommendedAreaCueLabel } from "./learningFormat";

export function LearningEntryPanel({
  onSelectArea,
}: {
  onSelectArea: (areaId: AreaId) => void;
}) {
  const [page, setPage] = useState<StudentLearningPageResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError("");
    getStudentLearningPage(null)
      .then((payload) => {
        if (!cancelled) setPage(payload);
      })
      .catch((requestError) => {
        if (!cancelled) setError(errorMessage(requestError));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const profiles = page?.profiles || [];
  const recommendedProfileId = page?.recommended_profile_id || page?.active_profile?.profile_id || profiles[0]?.profile_id || "";
  const recommendedProfile = profiles.find((profile) => profile.profile_id === recommendedProfileId) || profiles[0] || null;
  const recommendedArea = recommendedProfile ? profileAreaId(recommendedProfile) : null;
  const entryArea = recommendedArea || (profiles[0] ? profileAreaId(profiles[0]) : null) || "p";
  const recommendedCueLabel = formatRecommendedAreaCueLabel(recommendedProfile);
  const recommendedElementSymbols = useMemo(
    () => new Set<string>(recommendedProfile?.element_symbols || []),
    [recommendedProfile],
  );
  const entryAreaLearnableSymbols = useMemo(() => {
    const symbols = new Set<string>();
    profiles
      .filter((profile) => profileAreaId(profile) === entryArea)
      .forEach((profile) => {
        profile.element_symbols.forEach((symbol) => symbols.add(symbol));
      });
    return symbols;
  }, [entryArea, profiles]);

  return (
    <section className="learning-panel" aria-label="元素周期表章节入口">
      {loading ? <LearningState icon={<LoaderCircle className="spin" size={23} />} text="正在加载学习章节" /> : null}
      {error ? <LearningState icon={<FlaskConical size={23} />} text={error} /> : null}
      {!loading && !error ? (
        <PeriodicTable
          selectedArea={entryArea}
          recommendedArea={recommendedArea}
          recommendedCueLabel={recommendedCueLabel}
          recommendedSymbols={recommendedElementSymbols}
          learnableSymbols={entryAreaLearnableSymbols}
          onSelectArea={onSelectArea}
        />
      ) : null}
    </section>
  );
}
