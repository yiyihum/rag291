---
pretty_name: IoT & Cybersecurity Knowledge Graph
tags:
- knowledge-graph
- iot
- cybersecurity
- network-traffic
- botnet-detection
- building-automation
- multi-domain
- pretraining
license: mit
---

# IoT & Cybersecurity Knowledge Graph

This dataset is a unified knowledge graph constructed from various Hugging Face datasets focusing on IoT and Cybersecurity domains. It integrates structured and semi-structured data to provide a comprehensive view of network activities, device behaviors, cyberattacks, and building automation systems.

## Dataset Description

The primary goal of this dataset is to facilitate research and development in areas such as:
*   **IoT Security:** Understanding device vulnerabilities, attack patterns, and botnet activities.
*   **Network Anomaly Detection:** Providing rich contextual information for identifying unusual network behaviors.
*   **Building Automation:** Modeling relationships between sensors, HVAC systems, and building infrastructure using established ontologies like Brick.
*   **Knowledge Graph Embeddings (KGE):** Serving as a diverse input for training KGE models.
*   **Large Language Model Pre-training:** Providing structured knowledge for enhancing LLMs in specialized domains.

The dataset is built by processing and extracting entities and relations from the following source datasets (as specified in `pipeline/iot.json`):
*   `codymlewis/TON_IoT_network`
*   `rnaveensrinivas/NF-ToN-IoT-Attack_details`
*   `yashika0998/iot-23-preprocessed`
*   `codymlewis/nbaiot`
*   `gtfierro/mortar`
*   `JimXie/IIoTset`
*   *(and potentially others as defined in `pipeline/iot.json`)*

## Dataset Structure

The dataset is provided in **JSON Lines (`.jsonl`)** format. Each line in the file represents a single **triple** (subject, predicate, object), forming a statement in the knowledge graph.

Example triple format:
```json
{"subject": "entity_id_1", "predicate": "relation_type", "object": "entity_id_2"}
```
or for attributes:
```json
{"subject": "entity_id", "predicate": "has_attribute", "object": "attribute_value"}
```

## Data Fields (Entities and Relations)

The knowledge graph contains a diverse set of entities and relations, including but not limited to:

### Entities:
*   **Network-related:** `IPAddress`, `Port`, `Protocol`, `Service`, `NetworkConnection`, `NetworkFlowSequence`, `NetworkPacket`, `NetworkMetric`, `NetworkConcept`.
*   **IoT Devices:** `IoTDevice`, `IIoTDevice`.
*   **Cybersecurity:** `AttackType`, `CyberAttackConcept`, `AttackTechnique`, `VulnerabilityType`, `MitigationMeasure`, `ThreatActor`, `DataBreach`, `InformationType`, `TargetSystem`, `Impact`.
*   **Building Automation:** `Building`, `Sensor`, `HVACSystem`, `LightingSystem`, `SensorReading`, `BrickURI`.
*   **Temporal:** `Timestamp`.

### Relations (Predicates):
*   **Network Flow:** `has_source_ip`, `has_destination_ip`, `has_source_port`, `has_destination_port`, `uses_protocol`, `uses_service`, `has_duration`, `has_src_bytes`, `has_dst_bytes`, `has_connection_state`, `is_type`, `has_timestamp`, `has_unique_id`, `has_originating_host`, `has_responding_host`, `is_local_origin`, `is_local_response`, `contains_packet`, `has_frame_length`, `has_ip_length`, `has_ttl`, `has_ip_flag`, `has_data_length`, `uses_udp_port`, `has_dns_query_count`, `has_tcp_flag`, `has_tcp_port`, `has_attack_label`, `has_score`, `has_level`, `has_mqtt_length`, `has_nbns_flag`, `has_vnc_presence`, `has_ntp_root_dispersion`.
*   **Cyberattack Concepts:** `has_description`, `involves_technique`, `exploits_vulnerability`, `can_be_mitigated_by`, `targets`, `leads_to_impact`, `is_part_of`, `suffered_data_breach`, `involved_in`, `compromised`, `attributed_to`, `provides_answer_to`, `related_to`.
*   **IoT Device/Attack:** `originated_from_device`, `is_classified_as_attack`, `generates_traffic_of_type`.
*   **Building/Sensor:** `has_sensor`, `has_system`, `records_reading`, `has_value`, `has_timestamp`, `measures_property`, `uses_schema`.
*   **Network Metrics:** `has_description`, `relates_to_concept`, `helps_identify`, `indicates`.

## Usage

To generate this dataset, run the `main_pipeline.py` script located in the `pipeline/` directory. This script will download (or use local samples of) the specified datasets, process them, and output the unified knowledge graph in `data/unified_kg.jsonl`.

```bash
python pipeline/main_pipeline.py
```

## Licensing Information

This dataset is licensed under the Apache-2.0 License. Individual source datasets may have their own licenses; users are encouraged to review the licenses of the original datasets if they intend to use specific subsets.

## Citation Information

*(To be populated once the dataset is published)*