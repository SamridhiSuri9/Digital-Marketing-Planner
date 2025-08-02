from workflows.campaign_workflow import run_campaign_workflow

if __name__ == "__main__":
    topic = "Eco-Friendly Water Bottles"
    print(f"🚀 Running Digital Marketing Planner for: {topic}")

    result = run_campaign_workflow(topic)
    

    print("\n🎯 Final Output:\n")
    print("Target Audience:\n", result["Target Audience"])
    print("\nContent Strategy:\n", result["Content Strategy"])
    print("\nMarketing Posts:\n", result["Marketing Posts"])

