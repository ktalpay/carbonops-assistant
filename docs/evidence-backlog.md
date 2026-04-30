# Evidence Backlog (Next 30 Days)

## Purpose
This backlog tracks evidence-oriented work to improve deterministic quality and traceability for the next development phase.

## Planned tasks

1. **Expand evaluation cases by scenario family**  
   - GTV relevance: improves repeatable validation evidence  
   - Risk: Medium  
   - Notes: add grouped cases for missing units, ambiguous factors, and unsupported certification phrasing.

2. **Expand evaluation diff reporting surface carefully**  
   - GTV relevance: supports transparent run-to-run comparisons while preserving deterministic behavior  
   - Risk: Medium  
   - Notes: evaluate whether additional stable fields beyond status/case-id transitions are needed.

3. **Tighten orchestrator response regression tests**  
   - GTV relevance: demonstrates stable behavior boundaries  
   - Risk: Medium  
   - Notes: add snapshots for status, limitations, and sources formatting.

4. **Add knowledge-base content review checklist**  
   - GTV relevance: improves consistency and evidence quality in local knowledge files  
   - Risk: Low  
   - Notes: include prohibited claims, assumption clarity, and source-path traceability checks.

5. **Prepare small domain-specific example pack**  
   - GTV relevance: creates concrete examples for deterministic behavior assessment  
   - Risk: Medium  
   - Notes: include electricity, fuel, and freight mini-cases with explicit assumptions.

6. **Draft Hugging Face readiness notes (non-publishing)**  
   - GTV relevance: prepares structured metadata expectations for future dataset/model-card work  
   - Risk: Low  
   - Notes: define fields, limitations language, and provenance expectations without publishing.

## Non-goals for this backlog window

- No claims of completion or production readiness
- No external API integrations
- No regulatory/compliance certification claims
- No deployment/publishing automation

## Candidate issue titles

- `COA: Add grouped deterministic evaluation edge cases`
- `COA: Emit deterministic evaluation summary artifact`
- `COA: Add orchestrator response regression fixtures`
- `COA: Add knowledge-base conservative content checklist`
- `COA: Add domain mini-case pack for local evidence`
- `COA: Draft HF dataset/model-card readiness notes`

## Recently completed (2026-04-30)

- Scenario-family evaluation files for guardrails, context gaps, assumptions, and calculation readiness
- Deterministic evaluation summary object with stable JSON output
- Snapshot save/load helpers for deterministic evaluation report artifacts
- Deterministic evaluation diff module and CLI `compare-evaluations` command
- Local CLI `evaluate` command with pass/fail exit codes

## Remaining limitations

- No LLM/model quality measurement
- No regulatory/compliance/certification claims
- No complete emissions accounting coverage
