# Protocol Operations Sections (9-12)

---

## Section 9: Statistical Considerations

### 9.1 Sample Size Determination

#### 9.1.1 Primary Analysis Assumptions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Primary Endpoint | Time to first MACE | Composite of CV death, MI, stroke |
| Expected Event Rate (Placebo) | 15% | Based on AQUATIC, COMPASS trials |
| Expected Event Rate (Aspirin) | 11.25% | 25% relative risk reduction |
| Significance Level (α) | 0.05 | Two-sided |
| Statistical Power (1-β) | 80% | Standard for Phase 4 trials |
| Allocation Ratio | 1:1 | Equal randomization |

#### 9.1.2 Sample Size Calculation Results

| Scenario | N per Group | Total N |
|----------|-------------|---------|
| 20% RRR, 80% power | 2,036 | 4,072 |
| **25% RRR, 80% power (Selected)** | 1,000 | 2,000 |
| 20% RRR, 90% power | 2,726 | 5,452 |

**Selected Sample Size: 2,000 participants (1,000 per arm)**

#### 9.1.3 Rationale for Selected Sample Size

- Consistent with similar trials (AQUATIC planned N=2,000)
- Adequate power to detect clinically meaningful 25% relative risk reduction
- Feasible enrollment within reasonable timeframe
- Sufficient for safety evaluation
- 10% dropout adjustment incorporated

### 9.2 Analysis Populations

| Population | Definition | Primary Use |
|------------|------------|-------------|
| **Intent-to-Treat (ITT)** | All randomized participants | Primary efficacy analysis |
| **Modified ITT (mITT)** | Randomized participants who received ≥1 dose and had ≥1 post-baseline assessment | Supportive efficacy |
| **Per-Protocol (PP)** | mITT without major protocol deviations | Sensitivity analysis |
| **Safety Population** | All participants who received ≥1 dose of study drug | Safety analysis |

### 9.3 Primary Analysis

#### 9.3.1 Statistical Method

- **Primary Endpoint:** Time to first MACE
- **Analysis Method:** Cox proportional hazards regression
- **Stratification:** Randomization strata (prior PCI, diabetes, age, region)
- **Hazard Ratio:** Aspirin vs. Placebo with 95% CI
- **Statistical Test:** Log-rank test (stratified)

#### 9.3.2 Primary Hypothesis

- **Null Hypothesis (H₀):** HR = 1.0 (no difference)
- **Alternative Hypothesis (H₁):** HR ≠ 1.0
- **Significance Level:** α = 0.05 (two-sided)

#### 9.3.3 Kaplan-Meier Analysis

- Survival curves will be generated for each treatment group
- Median time-to-event and landmark event rates at 12 and 24 months
- 95% confidence intervals using Greenwood's formula

### 9.4 Secondary Analyses

| Endpoint | Analysis Method |
|----------|-----------------|
| Individual MACE components | Cox regression, Kaplan-Meier |
| All-cause mortality | Cox regression, log-rank test |
| Coronary revascularization | Cox regression |
| Major bleeding (BARC 3-5) | Cox regression |
| Quality of life (EQ-5D, SAQ) | MMRM, change from baseline |

### 9.5 Subgroup Analyses

Pre-specified subgroups (exploratory, not powered for statistical significance):

| Subgroup | Categories |
|----------|------------|
| Age | ≤65 years vs. >65 years |
| Sex | Male vs. Female |
| Prior PCI | Yes vs. No |
| Diabetes mellitus | Yes vs. No |
| Renal function | eGFR ≥60 vs. <60 mL/min |
| Baseline statin use | Yes vs. No |
| Geographic region | North America, Europe, Asia-Pacific |

Interaction tests (treatment × subgroup) will be performed. Forest plots will display subgroup-specific hazard ratios.

### 9.6 Multiplicity Adjustment

- Primary endpoint tested at α = 0.05
- Secondary endpoints: hierarchical testing procedure
- Subgroup analyses: exploratory, no multiplicity adjustment

### 9.7 Handling of Missing Data

| Situation | Approach |
|-----------|----------|
| Lost to follow-up (vital status) | Multiple imputation for sensitivity |
| Missing baseline covariates | Multiple imputation |
| Missing endpoint data | Sensitivity analysis (worst-case, best-case) |
| Withdrawn from treatment | Follow for outcomes (ITT principle) |

### 9.8 Interim Analyses

- **Number:** One formal interim analysis at 50% information fraction
- **Spending Function:** O'Brien-Fleming boundary (Lan-DeMets)
- **Alpha Spent:** ~0.003 at interim, ~0.049 at final
- **Review:** Data Safety Monitoring Board (DSMB)

---

## Section 10: Safety Monitoring

### 10.1 Adverse Event Definitions

#### 10.1.1 Adverse Event (AE)

Any untoward medical occurrence in a participant administered study drug, regardless of causal relationship.

#### 10.1.2 Serious Adverse Event (SAE)

An AE that:
- Results in death
- Is life-threatening
- Requires hospitalization or prolongation of hospitalization
- Results in persistent or significant disability/incapacity
- Is a congenital anomaly/birth defect
- Is a medically important event

#### 10.1.3 Adverse Events of Special Interest (AESI)

| Category | Events |
|----------|--------|
| **Bleeding** | All BARC Type ≥2 bleeding |
| **Gastrointestinal** | GI ulceration, perforation, obstruction |
| **Hypersensitivity** | Allergic reactions, anaphylaxis, angioedema |
| **Renal** | Acute kidney injury, significant creatinine increase |
| **Hepatic** | ALT/AST >3× ULN, drug-induced liver injury |

### 10.2 Adverse Event Collection and Reporting

| Event Type | Collection Period | Reporting Timeline |
|------------|-------------------|-------------------|
| All AEs | Randomization to 30 days post last dose | At each visit |
| SAEs | Consent to 30 days post last dose | Within 24 hours |
| AESIs | Randomization to 30 days post last dose | Within 72 hours |

### 10.3 Causality Assessment

Investigators will assess relationship to study drug:

| Assessment | Definition |
|------------|------------|
| Related | Reasonable possibility of causal relationship |
| Not Related | No reasonable possibility of causal relationship |

### 10.4 Data Safety Monitoring Board (DSMB)

#### 10.4.1 Composition

- Independent statistician (Chair)
- Two cardiologists with clinical trial experience
- One expert in clinical trial safety
- Non-voting members: Sponsor medical monitor, independent statistician

#### 10.4.2 DSMB Responsibilities

1. Review accumulating safety data (unblinded)
2. Monitor for unexpected safety signals
3. Conduct interim efficacy analysis
4. Recommend:
   - Continuation without modification
   - Protocol modification
   - Early termination for safety, futility, or efficacy

#### 10.4.3 DSMB Meeting Schedule

| Meeting Type | Frequency |
|--------------|-----------|
| Organizational | Before first participant enrolled |
| Safety reviews | Every 6 months |
| Interim analysis | At 50% information (events) |
| Ad hoc | As needed for safety concerns |

### 10.5 Stopping Rules

#### 10.5.1 Safety Stopping

The DSMB may recommend stopping if:
- Significant excess mortality in aspirin arm (p < 0.01)
- Significant excess major bleeding (≥2-fold increase, p < 0.01)
- Unexpected safety signal requiring action

#### 10.5.2 Efficacy Stopping

Early termination for efficacy at interim analysis if:
- Log-rank p-value crosses O'Brien-Fleming boundary
- Benefit-risk assessment favorable

#### 10.5.3 Futility Stopping

Conditional power <10% at interim analysis may trigger futility assessment.

---

## Section 11: Data Management

### 11.1 Data Collection System

| Component | Specification |
|-----------|---------------|
| Electronic Data Capture (EDC) | Validated, 21 CFR Part 11 compliant |
| Database | Oracle Clinical / Medidata Rave |
| Audit Trail | Complete, tamper-proof |
| User Access | Role-based, password protected |

### 11.2 Case Report Forms (CRFs)

Electronic CRFs will capture:
- Demographics and baseline characteristics
- Medical history
- Eligibility criteria verification
- Study drug exposure and compliance
- Concomitant medications
- Efficacy assessments (endpoint events)
- Safety data (AEs, laboratory results)
- Protocol deviations

### 11.3 Data Entry and Validation

| Process | Description |
|---------|-------------|
| Real-time validation | Range checks, consistency checks |
| Query management | Automated and manual queries |
| Source data verification | 100% of primary endpoint data |
| Data review | Medical monitor review of safety data |

### 11.4 Endpoint Adjudication

#### 11.4.1 Clinical Events Committee (CEC)

- Independent committee blinded to treatment
- Cardiologists and neurologists
- Adjudicates all potential MACE and bleeding events

#### 11.4.2 Adjudication Process

1. Site reports potential event
2. Source documents collected
3. CEC reviews blinded data
4. Consensus adjudication
5. Database updated with adjudicated outcomes

### 11.5 Database Lock

| Step | Timeline |
|------|----------|
| Last participant last visit | Day 0 |
| Query resolution | 4 weeks |
| Medical coding completion | 6 weeks |
| Database lock | 8 weeks |

### 11.6 Data Quality Assurance

- Regular data quality reports
- Site monitoring visits (risk-based)
- Central statistical monitoring
- Annual quality audits

---

## Section 12: Administrative Procedures

### 12.1 Regulatory Requirements

#### 12.1.1 IRB/Ethics Committee Approval

- Protocol, ICF, and recruitment materials require IRB/EC approval
- Approval obtained before site initiation
- Annual continuing review
- Amendments require approval before implementation

#### 12.1.2 Regulatory Authority Notifications

| Region | Authority | Requirement |
|--------|-----------|-------------|
| USA | FDA | IND submission (may qualify for IND exemption for approved drug) |
| EU | EMA/National | EudraCT registration, national authority notification |
| Japan | PMDA | Clinical trial notification |

### 12.2 Informed Consent Process

#### 12.2.1 Consent Requirements

- Written informed consent required before any study procedures
- Consent obtained by qualified site personnel
- Participant receives signed copy
- Re-consent required for significant protocol amendments

#### 12.2.2 Consent Elements

- Study purpose and procedures
- Risks and benefits
- Alternative treatments
- Confidentiality protections
- Voluntary participation
- Right to withdraw
- Contact information

### 12.3 Protocol Amendments

| Amendment Type | Process |
|----------------|---------|
| Substantial | IRB/EC and regulatory approval before implementation |
| Administrative | Notification to IRB/EC, immediate implementation allowed |

### 12.4 Protocol Deviations

| Category | Definition | Reporting |
|----------|------------|-----------|
| Important | May affect safety, rights, or data integrity | Within 24 hours |
| Minor | Does not affect above | Monthly summary |

### 12.5 Study Documentation

#### 12.5.1 Essential Documents

- Signed protocol and amendments
- IRB/EC correspondence and approvals
- Regulatory authority correspondence
- Informed consent forms
- Investigator's Brochure
- Monitoring reports
- Delegation logs

#### 12.5.2 Record Retention

- Minimum 15 years after study completion
- Per local regulatory requirements (whichever longer)

### 12.6 Publication Policy

- Results will be published regardless of outcome
- Primary manuscript in peer-reviewed journal
- ClinicalTrials.gov results posting within 12 months of study completion
- Authorship per ICMJE guidelines

### 12.7 Study Termination

#### 12.7.1 Early Termination Criteria

The study may be terminated if:
- DSMB recommendation for safety
- Regulatory authority mandate
- Sponsor decision (futility, operational reasons)
- Inability to enroll adequate participants

#### 12.7.2 Termination Procedures

1. Notify IRB/EC and regulatory authorities
2. Notify investigators and participants
3. Ensure participant safety and appropriate care transition
4. Complete data collection for enrolled participants (when possible)
5. Database lock and final analysis

### 12.8 Insurance and Indemnification

- Sponsor provides clinical trial insurance
- Coverage for study-related injuries
- Participants informed of compensation provisions

---

**Document Control:**
- Version: 1.0
- Date: 2026-01-14
- Status: Draft - For Review

---
