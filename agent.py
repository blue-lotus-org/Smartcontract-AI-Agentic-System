# PIPLINE AGENTIC METHOD
# pip install request os
import requests
import os

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

class MistralAgent:
    """Base class for AI-powered agents."""
    def __init__(self, role, model="mistral-large-latest"):
        self.role = role
        self.model = model

    def query_mistral(self, prompt):
        """Calls the Mistral API with a given prompt."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MISTRAL_API_KEY}"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": self.role}, {"role": "user", "content": prompt}],
            "temperature": 0.2
        }
        
        response = requests.post(MISTRAL_ENDPOINT, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            return f"Error: {response.status_code}, {response.text}"

# 🔹 Define Agents
class RequirementsAgent(MistralAgent):
    def __init__(self):
        super().__init__("You gather and refine user requirements for smart contracts.")

class GenerationAgent(MistralAgent):
    def __init__(self):
        super().__init__("You generate secure and efficient Solidity smart contracts.")

class SecurityAuditorAgent(MistralAgent):
    def __init__(self):
        super().__init__("You analyze Solidity code for security vulnerabilities and suggest fixes.")

class OptimizationAgent(MistralAgent):
    def __init__(self):
        super().__init__("You optimize Solidity code for gas efficiency and readability.")

class DeploymentAgent(MistralAgent):
    def __init__(self):
        super().__init__("You generate deployment scripts and verify contract readiness.")

# 🔹 Team Collaboration
def multi_agent_smart_contract_pipeline(user_input):
    """Orchestrates multiple AI agents to generate, audit, optimize, and deploy smart contracts."""
    
    # Step 1: Gather and refine requirements
    requirements_agent = RequirementsAgent()
    refined_requirements = requirements_agent.query_mistral(user_input)
    
    # Step 2: Generate smart contract
    generation_agent = GenerationAgent()
    raw_contract = generation_agent.query_mistral(refined_requirements)
    
    # Step 3: Security audit
    auditor_agent = SecurityAuditorAgent()
    security_report = auditor_agent.query_mistral(f"Analyze this Solidity contract:\n{raw_contract}")
    
    # Step 4: Optimization
    optimization_agent = OptimizationAgent()
    optimized_contract = optimization_agent.query_mistral(f"Optimize this Solidity contract:\n{raw_contract}")
    
    # Step 5: Deployment preparation
    deployment_agent = DeploymentAgent()
    deployment_script = deployment_agent.query_mistral(f"Generate a deployment script for:\n{optimized_contract}")

    # Output results
    return {
        "Refined Requirements": refined_requirements,
        "Generated Smart Contract": raw_contract,
        "Security Audit Report": security_report,
        "Optimized Smart Contract": optimized_contract,
        "Deployment Script": deployment_script
    }

# 🚀 Run the pipeline
if __name__ == "__main__":
    user_input = input("Enter your smart contract requirements: ")
    results = multi_agent_smart_contract_pipeline(user_input)

    print("\n🔹 Refined Requirements:\n", results["Refined Requirements"])
    print("\n🔹 Generated Smart Contract:\n", results["Generated Smart Contract"])
    print("\n🔹 Security Audit Report:\n", results["Security Audit Report"])
    print("\n🔹 Optimized Smart Contract:\n", results["Optimized Smart Contract"])
    print("\n🔹 Deployment Script:\n", results["Deployment Script"])

# Credits: 
#  Blue Lotus "https://lotuschain.org"
#  Mistral AI
