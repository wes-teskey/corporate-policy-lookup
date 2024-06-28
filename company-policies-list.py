# company_policies.py

def get_policies_list():
    return [
        # Software Company Specific
        "Employee Onboarding Process",
        "Incident Response Plan",
        "Product Development Lifecycle",
        "Customer Service Escalation Procedure",
        "Change Management Process",
        "Procurement Workflow",
        "Performance Review Cycle",
        "Data Backup and Recovery Protocol",
        "Employee Expense Reimbursement Process",
        "Quality Assurance Testing Procedure",
        "Software Release Management Process",
        "Agile Sprint Workflow",
        "Code Review Procedure",
        "Continuous Integration/Continuous Deployment (CI/CD) Pipeline",
        "Bug Tracking and Resolution Process",
        "Data Privacy and GDPR Compliance Procedure",
        "Software License Management Policy",
        "User Access Control and Authentication Process",
        "API Version Deprecation and Sunset Policy",
        "Disaster Recovery and Business Continuity Plan",
        "Technical Debt Management Process",
        "Third-Party Library and Component Evaluation Policy",
        "Feature Flagging and A/B Testing Procedure",
        "Cloud Resource Allocation and Management Policy",
        "Secure Coding Guidelines and Practices",
        "Customer Data Handling and Retention Policy",
        "Incident Postmortem and Root Cause Analysis Process",
        "Software Architecture Review Procedure",
        "Dev/Staging/Production Environment Management Policy",
        "Open Source Contribution Guidelines",

        # General Policies
        "Remote Work Policy",
        "Employee Training and Development Program",
        "Workplace Health and Safety Guidelines",
        "Diversity, Equity, and Inclusion (DEI) Policy",
        "Corporate Social Responsibility (CSR) Framework",
        "Conflict Resolution Procedure",
        "Internal Communication Strategy",
        "Intellectual Property Protection Policy",
        "Vendor Management Process",
        "Environmental Sustainability Practices",
        "Employee Leave and Time-Off Policy",
        "Business Travel and Expense Management",
        "Anti-Harassment and Non-Discrimination Policy",
        "Information Security and Data Protection Guidelines",
        "Performance Management and Appraisal Process",
        "Employee Grievance Procedure",
        "Asset Management and Inventory Control",
        "Corporate Governance Structure",
        "Crisis Management and Emergency Response Plan",
        "Ethical Business Conduct and Compliance Policy"
    ]

# You can test the function here
if __name__ == "__main__":
    policies = get_policies_list()
    for i, policy in enumerate(policies, 1):
        print(f"{i}. {policy}")
