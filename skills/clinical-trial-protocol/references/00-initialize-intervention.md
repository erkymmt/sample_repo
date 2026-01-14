# Step 0: Initialize Intervention

## Purpose
Collect and validate intervention information from the user.

## Instructions

1. **Ask the user for intervention details:**
   - Intervention type: Device or Drug?
   - Name of the intervention
   - Target indication/condition
   - Brief description of mechanism of action
   - Any existing regulatory status (if applicable)

2. **Validate the information:**
   - Ensure all required fields are provided
   - Confirm with user before proceeding

3. **Save to waypoint:**
   Create `waypoints/intervention_metadata.json` with:
   ```json
   {
     "intervention_name": "",
     "intervention_type": "device|drug",
     "indication": "",
     "mechanism_of_action": "",
     "regulatory_status": "",
     "initial_context": "",
     "created_at": "",
     "completed_steps": ["0"]
   }
   ```

4. **Confirm completion:**
   Display: "✓ Step 0 complete - Intervention initialized"
