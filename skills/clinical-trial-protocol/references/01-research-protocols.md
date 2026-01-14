# Step 1: Research Similar Protocols

## Purpose
Research similar clinical trials, FDA guidance, and regulatory pathways.

## Prerequisites
- clinical trials MCP Server must be available
- `waypoints/intervention_metadata.json` must exist

## Instructions

1. **Load intervention metadata:**
   Read `waypoints/intervention_metadata.json`

2. **Search for similar clinical trials:**
   Use `search_clinical_trials` MCP tool with:
   - condition: [indication from metadata]
   - intervention: [intervention name/type]
   - status: "all"
   - max_results: 25

3. **Analyze top results:**
   For each relevant trial, note:
   - NCT ID
   - Study design
   - Phase
   - Primary endpoints
   - Sample size
   - Key eligibility criteria

4. **Research FDA regulatory pathway:**
   Based on intervention type:
   - **Device:** 510(k), PMA, or De Novo pathway
   - **Drug:** IND, NDA, or BLA pathway

5. **Save research summary:**
   Create `waypoints/01_clinical_research_summary.json` with:
   - Similar trials list (top 10)
   - Recommended regulatory pathway
   - Key study design recommendations
   - Endpoint suggestions

6. **Update metadata:**
   Add "1" to completed_steps array

7. **Display completion:**
   "✓ Step 1 complete - Research summary generated"
