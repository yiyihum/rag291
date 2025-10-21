---
license: mit
task_categories:
- text-generation
- reinforcement-learning
tags:
- AI
- agent
---

# AI Agent Marketplace & Store Index An Open Source Collections of AI Agent Meta and Metric information

[Github](https://github.com/AI-Agent-Hub/AI-Agent-Marketplace)| [Huggingface](https://huggingface.co/datasets/DeepNLP/AI-Agent-Marketplace-Index) | [Pypi](https://pypi.org/project/ai-agent-marketplace/) | [Open Source AI Agent Marketplace & Store](https://www.deepnlp.org/store/ai-agent) | [Agent RL Dataset](https://www.deepnlp.org/store/dataset)

### AI Agent Marketplace Index DataSet

This DeepNLP AI Agent Marketplace dataset contains more than 10k+ AI Agent Meta information covering 30+ categories from Open AI Agent Marketplace (https://www.deepnlp.org/store/ai-agent).
We want to build an Open AI agent marketplace registry so that developers and can [submit their AI agent](https://www.deepnlp.org/workspace/my_ai_services) and users can explore. And we are providing 
the meta back to the community on a regular basis so the dataset is useful for research, development purposes.

<img src="https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/ai_agent_marketplace_distribution.png" style="height:600px;" alt="AI Agent Marketplace Category">

|  Dataset  |  Size  |  Last Upate Date  |
| ---- | ----- |  ---- |
| deepnlp_open_ai_agent_marketplace_index_2025_10.json | 14k |  2025-10-13  |


We would like to help developers and end users within the lifecycle of AI agent development. From the registration, deployment, Agent router, API calling, metric/traffic tracking, and finally to the stage of moneyterization from your AI Agent. Anyone can submit their AI agents card information, code, APIs, pricing plans to the public registry, just like your submit a paper to arxiv.org and submit models to huggingface.co.


- **Easy method to Submit** (python, nodejs and curl) for developers to submit their AI agents's meta information and register to the marketplace. Any user can explore and find their AI agents from the AI Agent search engine (https://www.deepnlp.org/search/agent) and API documentation (https://www.deepnlp.org/doc/ai_agent_marketplace). 


Users can submit their AI agent' meta information to deepnlp.org easily, just like how they submit papers to arxiv.org and submit models to huggingface.co. 

We aim to helo tackle the problem of tracking how many AI Agents are actively running in the world and track their performance (search rank/github star/API calls from Routers), collect users' reviews, etc and more. 


How to Use 

- The dataset will be useful for AI agent related research to project trending and analysis.  
- See Growth in different category, such as AI search agent, Coding Agent, GUI agent, Healthcare Agent, etc.
- Easy Usage of the json files updated on monthly basis and API access to latest AI agent metas (limitation)
- Welcome to add Backlink to this project.

Not to Use in this way
- Copy and paste without references


#### AI Agent Card Schema

agent.json example

For instance, we use the AI Agent MCP server [Google Maps MCP Servers](https://www.deepnlp.org/store/mcp-server/map/pub-google-maps/google-maps) as an example. 

```
{
  "unique_id": "google-maps/google-maps",
  "content_id": "b95c8ce38b3647069d9272a6c84d14a6",
  "content_name": "Google Maps",
  "category": "Map",
  "field": "MCP SERVER",
  "field_url": "mcp-server",
  "subfield": "Map",
  "subfield_url": "map",
  "content_tag_list": "official",
  "review_cnt": "2",
  "rating": "4.5",
  "GitHub Star": "69901",
  "Bing Rank": "",
  "Google Rank": "",
  "website": "",
  "github": "https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps",
  "detail_url": "https://www.deepnlp.org/store/mcp-server/map/pub-google-maps/google-maps"
}
```


**AI Agent Registry Data Sources**:
- Users' Registry and submission [GitHub](https://github.com/AI-Agent-Hub/AI-Agent-Marketplace).
- AI Agent open sourced in Github and more
- AI Agent in Each Store OpenAI SDK, Claude SDK, Modelscope, etc.
- Search Engine (Google/Bing)


### Submit AI Agent to Registry

**Curl**

Get Access Key (https://www.deepnlp.org/workspace/keys)
```
curl -X POST https://www.deepnlp.org/api/ai_agent_marketplace/registry -H "Content-Type: application/json" -d '{"github":"https://github.com/microsoft/markitdown", "access_key":"{AI_AGENT_MARKETPLACE_ACCESS_KEY}"}' 

```

**Python**
```
import ai_agent_marketplace as aa
import json

def publish_your_agent():
    """
        Submit Your AI Agent from Web: http://www.deepnlp.org/workspace/my_ai_services

        Using Command Lines: access_key can be obtained from your personal page:
        Keys: https://www.deepnlp.orgworkspace/keys
        once you submit, it's pending approval and you can track the data then
    """
    access_key = "${your_access_key}"
    agent_name = "My First AI Agent"

    item_info = {}
    item_info["content"] = "This AI Agent can do complicated programming work for humans"
    item_info["website"] = "https://www.my_first_agent.com"
    item_info["field"] = "AI AGENT"
    item_info["subfield"] = "Coding Agent"
    item_info["content_tag_list"] = "coding,python"
    result = aa.add(access_key=access_key, name=agent_name, item_info=item_info)
    
    
    url = result["url"] if "url" in result else ""
    msg = result["msg"] if "msg" in result else ""
    print ("## DEBUG: AI Agent Marketplace Post msg is|%s" % str(msg))
    print ("## DEBUG: AI Agent Marketplace Post url is|%s" % str(url))

publish_your_agent()
```

### Search AI Agent from Marketplace

```
import ai_agent_marketplace as aa
import json

def search_ai_agent_traffic_data():

    result = aa.search(q="Coding Agent Jetbrains")
    print ("## DEBUG: search result is|%s" % str(result))

    result2 = aa.search(q="Coding Agent", limit=20, timeout=5)
    print ("## DEBUG: search result is|%s" % str(result2))

    result3 = aa.search(q="", limit=20, timeout=5)
    print ("## DEBUG: search result is|%s" % str(result3))

search_ai_agent_traffic_data()

```


Related:
- [Open AI Agent Marketplace](https://www.deepnlp.org/store/ai-agent) and [AI Agent Search Engine](https://www.deepnlp.org/search/agent)
- [AI Agent Registry and Submission](https://www.deepnlp.org/workspace/my_ai_services)
- [OneKey Agent Router to Track AI Agent APIs Performace](https://www.deepnlp.org/agent/onekey-ai-agent-router)