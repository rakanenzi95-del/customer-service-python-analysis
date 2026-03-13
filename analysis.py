import pandas as pd

df = pd.read_csv("customer_service_python_project_dataset.csv")

print(df.head())
print(df.shape)
df.shape
df.columns
df["Status"].value_counts()
import pandas as pd

df = pd.read_csv("customer_service_python_project_dataset.csv")

print(df.head())

print(df.shape)
print(df.columns)
print(df["Status"].value_counts())
print(df["Channel"].value_counts())
print(df["Priority"].value_counts())
print(df["Agent_Name"].value_counts())
print(df["CSAT"].mean())


agent_tickets = df.groupby("Agent_Name")["Ticket_ID"].count()

print("Tickets handled by each agent:")
print(agent_tickets)

best_agent = agent_tickets.idxmax()

print("Best performing agent:", best_agent)

agent_tickets = df.groupby("Agent_Name")["Ticket_ID"].count()

print("Tickets handled by each agent:")
print(agent_tickets)

best_agent = agent_tickets.idxmax()

print("Best performing agent:", best_agent)

channel_usage = df["Channel"].value_counts()

print("Tickets by Channel:")
print(channel_usage)

closed_tickets = df[df["Status"] == "Closed"].shape[0]
total_tickets = df.shape[0]

closure_rate = (closed_tickets / total_tickets) * 100

print("Closed Tickets:", closed_tickets)
print("Total Tickets:", total_tickets)
print("Closure Rate:", closure_rate)

priority_analysis = df["Priority"].value_counts()

print("Ticket Priority Distribution:")
print(priority_analysis)



print(df.columns)


resolution_time = df.groupby("Agent_Name")["Resolution_Time_Hours"].mean()

print("Average Resolution_Time_Hours:")
print(resolution_time)


print("\n--- Customer Support Performance Report ---")

# أفضل موظف حسب عدد التذاكر
top_agent_tickets = df["Agent_Name"].value_counts().idxmax()

# أفضل موظف حسب رضا العملاء
top_agent_csat = df.groupby("Agent_Name")["CSAT"].mean().idxmax()

# أسرع موظف في حل التذاكر
fastest_agent = df.groupby("Agent_Name")["Resolution_Time_Hours"].mean().idxmin()

print("Top Agent by Tickets:", top_agent_tickets)
print("Top Agent by Customer Satisfaction:", top_agent_csat)
print("Fastest Agent (Resolution Time):", fastest_agent)
