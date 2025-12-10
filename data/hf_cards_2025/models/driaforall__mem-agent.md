---
pipeline_tag: text-generation
library_name: transformers
---
# mem-agent

Based on [Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507), this model was trained using GSPO (Zheng et al., 2025) over an agent scaffold that is built around an Obisidian-like memory system and the tools required to interact with it. The model was trained on the following subtasks:
- Retrieval: Retrieving relevant information when needed from the memory system. In this subtask, we also trained the model on filtering the retrieved information and/or obfuscating it completely.
- Updating: Updating the memory system with new information.
- Clarification: Asking for clarification when the user query is not clear/contradicting with the information in the memory system.

The tools in the scaffold are:
```markdown
# File Operations
create_file(file_path: str, content: str = "") -> bool  # Auto-creates parent directories
update_file(file_path: str, old_content: str, new_content: str) -> Union[bool, str] # Returns True or error message
read_file(file_path: str) -> str
delete_file(file_path: str) -> bool
check_if_file_exists(file_path: str) -> bool

# Directory Operations
create_dir(dir_path: str) -> bool
list_files() -> str  # Shows tree structure of current working directory
check_if_dir_exists(dir_path: str) -> bool

# Utilities
get_size(file_or_dir_path: str) -> int  # Bytes; empty = total memory size
go_to_link(link_string: str) -> bool
```

In the scaffold, the model uses `<think>`, `<python>` and `<reply>` tags to structure its response. Using `<reply>` only when it's done interacting with the memory. The `<python>` block is executed in a sandbox with the tools and the results of the code block are returned in a `<result>` tag to the model, forming the agentic loop.

The model is also trained to be able to handle optional filters given by the user in between <filter> tags after the user query. These filters are used to filter the retrieved information and/or obfuscate it completely.


## Benchmark

We evaluated this model and a few other open & closed ones on our benchmark, **md-memory-bench**. We used o3 from OpenAI as the judge. All the other models except driaforall/mem-agent and Qwen/Qwen3-4B-Thinking-2507 were used through OpenRouter.s

| Model | Retrieval | Update | Clarification | Filter | Overall |
|-------|-----------|--------|---------------|--------|---------|
| qwen/qwen3-235b-a22b-thinking-2507 | 0.9091 | 0.6363 | 0.4545 | 1 | 0.7857 |
| driaforall/mem-agent | 0.8636 | 0.7272 | 0.3636 | 0.9167 | 0.75 |
| z-ai/glm-4.5 | 0.7727 | 0.8181 | 0.3636 | 0.9167 | 0.7321 |
| deepseek/deepseek-chat-v3.1 | 0.6818 | 0.5454 | 0.5454 | 0.8333 | 0.6607 |
| google/gemini-2.5-pro | 0.7273 | 0.4545 | 0.2727 | 1 | 0.6429 |
| google/gemini-2.5-flash | 0.7727 | 0.3636 | 0.2727 | 0.9167 | 0.625 |
| openai/gpt-5 | 0.6818 | 0.5454 | 0.2727 | 0.9167 | 0.625 |
| anthropic/claude-opus-4.1 | 0.6818 | 0 | 0.8181 | 0.5833 | 0.5536 |
| Qwen/Qwen3-4B-Thinking-2507 | 0.4545 | 0 | 0.2727 | 0.75 | 0.3929 |
| moonshotai/kimi-k2 | 0.3181 | 0.2727 | 0.1818 | 0.6667 | 0.3571 |

Our model, with only 4B parameters, is only second on the benchmark, beating all the open & closed models except for qwen/qwen3-235b-a22b-thinking-2507. The model achieves an overall score of 0.75, a significant improvement over the 0.3929 of the base Qwen model.

## Usage

The model, while can be used on its own, is recommended to be used as an MCP server to a bigger model, which can then be used to interact with the memory system. For this, you can check [our repo](https://github.com/firstbatchxyz/mem-agent-mcp/), which contains instructions for both an MCP setup and a cli standalone model usage.

### Memory

The model uses a markdown based memory system with links, inspired by Obsidian. The general structure of the memory is:
```
memory/
    ├── user.md
    └── entities/
        └── [entity_name_1].md
        └── [entity_name_2].md
        └── ...
```

- `user.md` is the main file that contains information about the user and their relationships, accompanied by links to the enity file in the format of `[[entities/[entity_name].md]]` per relationship. The link format should be followed strictly.
- `entities/` is the directory that contains the entity files.
- Each entity file follows the same structure as `user.md`.
- Modifying the memory manually does not require restarting the MCP server.

### Example user.md

```markdown
# User Information
- user_name: John Doe
- birth_date: 1990-01-01
- birth_location: New York, USA
- living_location: Enschede, Netherlands
- zodiac_sign: Aquarius

## User Relationships
- company: [[entities/acme_corp.md]]
- mother: [[entities/jane_doe.md]]
```

### Example entity files (jane_doe.md and acme_corp.md)

```markdown
# Jane Doe
- relationship: Mother
- birth_date: 1965-01-01
- birth_location: New York, USA
```

```markdown 
# Acme Corporation
- industry: Software Development
- location: Enschede, Netherlands
```

The model is trained on this memory standard and any fruitful use should be on a memory system that follows this standard. We have a few memory export tools for different sources like ChatGPT, Notion, etc. in our mcp server repo.

## References: 
- [GSPO](https://arxiv.org/pdf/2507.18071), Zheng et al., 2025