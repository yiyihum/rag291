---
license: cc0-1.0
task_categories:
- text-generation
- text-classification
language:
- en
tags:
- environment
- permitting
- nepa
size_categories:
- 100K<n<1M
---

# National Environmental Policy Act Text Corpus (NEPATEC2.0)

## Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
The National Environmental Policy Act of 1969, as amended (NEPA), is a major environmental law in the United States, requiring Federal agencies to consider and document potential environmental impacts before deciding on a proposed action. 
Modernization of NEPA and permitting processes faces significant challenges due to the lack of standardized formats and interoperable systems for organizing and sharing NEPA-related information across agencies. 
Much of the information gathered during NEPA reviews is written into documents such as categorical exclusions, environmental assessments, and environmental impact statements, then filed in predominately independent agency file stores that may or may not be publicly accessible. 
The application of metadata and data standards, such as those recommended by the Council on Environmental Quality (CEQ), to NEPA documents offers a shared vocabulary and structure for key entities like projects, processes, and documents that can streamline information exchange and enhance collaboration across systems. 
In this work, we publicly release NEPATEC2.0, an expanded corpus of public NEPA documents with associated metadata. 
NEPATEC2.0 consists of more than 120,000 documents from 60,000 projects prepared by more than 60 different agencies. 
Modeled to align with CEQ metadata standards, NEPATEC2.0 promotes consistency in environmental reviews and supports the ongoing effort to modernize permitting technologies by facilitating more transparent, efficient, and data-driven decision-making. 

- **Paper:** [PDF](https://www.pnnl.gov/sites/default/files/media/file/PNNL_PermitAI_NEPATECv2_Public_Release_20_08_25.pdf)
- **Curated by:** Pacific Northwest National Laboratory
- **Funded by :** Office of Policy, Department of Energy
- **Language(s) (NLP):** English
- **License:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/)

## Usage

To download and use the data using HuggingFace datasets library, use the following code

```
from datasets import load_dataset
dataset_ce = load_dataset("PNNL/NEPATEC2.0", data_files=["CE/*/*.jsonl"])
dataset_ea = load_dataset("PNNL/NEPATEC2.0", data_files=["EA/*/*.jsonl"])
dataset_eis = load_dataset("PNNL/NEPATEC2.0", data_files=["EIS/*/*.jsonl"])
```

Please skip using ```load_dataset("PNNL/NEPATEC2.0")``` as the CE, EA, and EIS JSONs have slight variations in formatting.

## Dataset Structure

```json
{
    "project": {
        "project_ID": "UNIQUE PROJECT ID FOR PUBLIC VERSION",
        "project_title": {
            "value": ""
        },
        "project_sector": {
            "value": ""
        },
        "project_type": {
            "value": ""
        },
        "project_description": {
            "value": ""
        },
        "project_sponsor": {
            "value": ""
        },
        "location": {
            "value": ""
        }
    },
    "process": {
        "process_family": {
            "value": ""
        },
        "process_type": {
            "value": ""
        },
        "lead_agency": {
            "value": ""
        }
    },
    "documents": [
        {
            "metadata": {
                "document_metadata":{
                    "document_ID": {
                        "value": "UNIQUE DOC/FILE ID FOR PUBLIC VERSION"
                    },
                    "document_type": {
                        "value": ""
                    },
                    "document_title": {
                        "value": ""
                    },
                    "prepared_by": {
                        "value": ""
                    },
                    "ce_category": {
                        "value": ""
                    }
                },
                "file_metadata":{
                    "file_ID": {
                        "value": "UNIQUE DOC/FILE ID FOR PUBLIC VERSION"
                    },
                    "file_name": {
                        "value": "PDF NAME"
                    },
                    "section_or_volume_title": {
                        "value": ""
                    },
                    "main_document": {
                        "value": ""
                    },
                    "total_pages": {
                        "value": ""
                    },
                    "file_provider": {
                        "value": ""
                    }
                }
            },
            "pages": [
                {
                    "page number": 1,
                    "page text": "PAGE 1 TEXT"
                },
                {
                    "page number": 2,
                    "page text": "PAGE 2 TEXT"
                }
            ]
        },
        {
            "metadata": {
                "file_metadata":{
                    "file_ID": {
                        "value": "UNIQUE DOC/FILE ID FOR PUBLIC VERSION"
                    },
                    "file_name": {
                        "value": "PDF NAME"
                    },
                    "section_or_volume_title": {
                        "value": ""
                    },
                    "main_document": {
                        "value": ""
                    },
                    "total_pages": {
                        "value": ""
                    },
                    "file_provider": {
                        "value": ""
                    }
                }
            },
            "pages": [
                {
                    "page number": 1,
                    "page text": "PAGE 1 TEXT"
                },
                {
                    "page number": 2,
                    "page text": "PAGE 2 TEXT"
                }
            ]
        }
    ]
}
```


Metadata attributes grouped by entity. All attributes are available across EIS, EA, and CE process types, except those marked with an asterisk (*), which are available only for CE processes.

| **Entity** | **Metadata Attribute** | **Description** | **Datatype** |
| :--- | :--- | :--- | :--- |
| **Process** | lead\_agency | Federal or other agency responsible for conducting the process. | text |
| **Process** | process\_family | Major category that the process belongs to. | text |
| **Process** | process\_type | Type of review or permitting process. A sub-type of process family. | text |
| **Project** | project\_title | Descriptive name of the project. | text |
| **Project** | location | Name of city, county, or other geographic area where the project is located. | text |
| **Project** | project\_sponsor | Name of responsible entity, organization, or person for project. | text |
| **Project** | project\_sector | High-level project sector(s). | text |
| **Project** | project\_type | Type(s) of project. A sub-type of project sector. See list in Table \ref{tab:types}. Categorization is based on best fit and is subjective. | text |
| **Document** | document\_type | Type of document. | text |
| **Document** | document\_title | Title of document, reflecting the actual title, not the file name. | text |
| **Document** | prepared\_by | Agency or entity (e.g., contractor) responsible for preparation. | text |
| **Document** | ce\_category* | Specific category or categories under which the action is classified as a CE. | text |
| **Document** | action\_description* | Brief summary of the proposed action, including its purpose and need. | text |
| **File** | section\_or\_volume\_title | Title of a specific document section or volume. | text |
| **File** | main\_document | Indicates if file is the main document ("Yes") or supporting info ("No"). Main document consists of the title page and executive summary through all chapters, but excludes appendices. | boolean |

### NEPATECv2 Dataset Statistics

| Metric         | Total Count   |
|----------------|--------------:|
| **Agencies**   | `60+`         |
| **Projects**   | `61,881`      |
| **Files**      | `142,083`     |
| **Pages**      | `6,967,739`   |


**Breakdown by NEPA Process**

| Process                         | Projects | Files   | Pages       |
|----------------------------------------|---------:|--------:|------------:|
| **Categorical Exclusion (CE)**         | 54,668   | 73,544  | 366,876     |
| **Environmental Assessment (EA)**      | 3,083    | 14,242  | 469,106     |
| **Environmental Impact Statement (EIS)**| 4,130    | 54,297  | 6,131,757   |

## Notice 
Released under the Creative Commons 0 Public Domain Dedication: https://creativecommons.org/publicdomain/zero/1.0/ 
This material is free to use, and attribution is always appreciated.  

Please cite the following in your work: 
```
@misc{NEPATECv2,  
author={Sai Munikoti, Dan Nally, Sai Dileep Koneru, Siddhartha Shankar Das, Kaustav Bhattacharjee, Ashik Islam, Alex Buchko, Taylor Edwards, Kathy Nwe, Siddhisanket Raskar, Paul Rigor, Heng Wan, Micah Taylor, Scott Spare, Derek Lilienthal, Mahantesh Halappanavar, Anurag Acharya, Tim Vega, Mike Parker, Anastasia Bernat, and Sameera Horawalavithana}, 
title={NEPATEC v2.0: Standardized Metadata and Text Corpus of National Environmental Policy Act Documents}, 
howpublished = "\url{https://www.pnnl.gov/sites/default/files/media/file/PNNL_PermitAI_NEPATECv2_Public_Release_20_08_25.pdf}}", 
year = {2025},  
note = "[Online; accessed 20-Aug-2025]" 
```

We welcome your feedback and suggestions to help improve this dataset. 
If you have any comments, or questions, please email us at [permitai@pnnl.gov](mailto:permitai@pnnl.gov).
 

## DISCLAIMER
This material was prepared as an account of work sponsored by an agency of the United States Government.  Neither the United States Government nor the United States Department of Energy, nor the Contractor, nor any or their employees, nor any jurisdiction or organization that has cooperated in the development of these materials, ***makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe privately owned rights.*** 

Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof. 

                 PACIFIC NORTHWEST NATIONAL LABORATORY
                              operated by
                                BATTELLE
                                for the
                   UNITED STATES DEPARTMENT OF ENERGY
                    under Contract DE-AC05-76RL01830
                    
## Acknowledgement

This work was supported by the Office of Policy, U.S. Department of Energy, and Pacific Northwest National Laboratory, which is operated by Battelle Memorial Institute for the U.S. Department of Energy under Contract DE-AC05–76RLO1830.