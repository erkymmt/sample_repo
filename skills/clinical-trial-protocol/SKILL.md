---
name: clinical-trial-protocol-skill
description: Generate clinical trial protocols for medical devices or drugs. This skill should be used when users say "Create a clinical trial protocol", "Generate protocol for [device/drug]", "Help me design a clinical study", "Research similar trials for [intervention]", or when developing FDA submission documentation for investigational products.
---

# Clinical Trial Protocol Skill

## ⚠️ EXECUTION CONTROL - READ THIS FIRST

**CRITICAL: This orchestrator follows a SIMPLE START approach:**

1. **Display the welcome message FIRST** (shown in "Startup: Welcome and Confirmation" section below)
2. **Ask user to confirm they're ready to proceed** - Wait for confirmation (yes/no)
3. **Jump directly into Full Workflow Logic** - Automatically run subskills sequentially
4. **Do NOT pre-read subskill files** - Subskills are loaded on-demand only when their step executes

**Why this matters:**
- Pre-reading all subskills wastes context and memory
- Subskills should only load when actually needed during execution
- Workflow automatically handles resuming from existing waypoints

## Overview

This skill generates clinical trial protocols for **medical devices or drugs** using a **modular, waypoint-based architecture**

## What This Skill Does

Starting with an intervention idea (device or drug), this orchestrated workflow offers two modes:

**🔬 Research Only Mode (Steps 0-1):**
0. **Initialize Intervention** - Collect device or drug information
1. **Research Similar Protocols** - Find similar trials, FDA guidance, and published protocols
   - **Deliverable:** Comprehensive research summary as formatted .md artifact

**📄 Full Protocol Mode (Steps 0-5):**
0. **Initialize Intervention** - Collect device or drug information
1. **Research Similar Protocols** - Find similar trials, FDA guidance, and published protocols
2. **Protocol Foundation** - Generate protocol sections 1-6 (foundation, design, population)
3. **Protocol Intervention** - Generate protocol sections 7-8 (intervention details)
4. **Protocol Operations** - Generate protocol sections 9-12 (assessments, statistics, operations)
5. **Generate Protocol** - Create professional file ready for stakeholder review

## Architecture

### Waypoint-Based Design

All analysis data is stored in `waypoints/` directory as JSON/markdown files:

```
waypoints/
├── intervention_metadata.json       # Intervention info, status, initial context
├── 01_clinical_research_summary.json # Similar trials, FDA guidance, recommendations
├── 02_protocol_foundation.md        # Protocol sections 1-6 (Step 2)
├── 03_protocol_intervention.md      # Protocol sections 7-8 (Step 3)
├── 04_protocol_operations.md        # Protocol sections 9-12 (Step 4)
├── 02_protocol_draft.md             # Complete protocol (concatenated in Step 4)
├── 02_protocol_metadata.json        # Protocol metadata
└── 02_sample_size_calculation.json  # Statistical sample size calculation
```

### Modular Subskill Steps

Each step is an independent skill in `references/` directory:

```
references/
├── 00-initialize-intervention.md    # Collect device or drug information
├── 01-research-protocols.md         # Clinical trials research and FDA guidance
├── 02-protocol-foundation.md        # Protocol sections 1-6
├── 03-protocol-intervention.md      # Protocol sections 7-8
├── 04-protocol-operations.md        # Protocol sections 9-12
└── 05-generate-document.md          # NIH Protocol generation
```

## Prerequisites

### 1. clinical trials MCP Server (Required)

**Available Tools:**
- `search_clinical_trials` - Search by condition, intervention, sponsor, location, status, phase
- `get_trial_details` - Get comprehensive details for a specific trial using its nct_id

### 2. Python Dependencies (Required for Step 2)

```bash
pip install scipy numpy
```

## How to Use

Simply invoke the skill and select your desired mode:

**🔬 Research Only Mode:**
1. Select "Research Only" from the main menu
2. Provide intervention information
3. Receive comprehensive research summary

**📄 Full Protocol Mode:**
1. Select "Full Protocol" from the main menu
2. Guide you through all steps sequentially (Steps 0-5)
3. Generate the final protocol document

## Disclaimers

⚠️ **IMPORTANT:** This protocol generation tool provides preliminary clinical study protocol based on NIH/FDA guidelines and similar trials. It does NOT constitute:
- Official FDA or IRB determination or approval
- Medical, legal, or regulatory advice
- Substitute for professional biostatistician review
- Substitute for FDA Pre-Submission meeting

**REQUIRED before proceeding with clinical study:**
- Biostatistician review and sample size validation
- FDA Pre-Submission meeting
- IRB review and approval
- Clinical expert and regulatory consultant engagement
