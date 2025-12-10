---
license: apache-2.0
language:
- vi
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
tags:
- retrieval-augmented-generation
- text-generation-inference
library_name: transformers
---

## Model Card: GRPO-VI-Qwen2-7B-RAG
 
**Model Description:**

GRPO-VI-Qwen2-7B-RAG is a large language model fine-tuned from the base model Qwen2.5-7B-Instruct (https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) to serve Retrieval-Augmented Generation (RAG) tasks. The fine-tuning process involves Supervised Fine-Tuning combined with GRPO (Group Relative Policy Optimization).

The model is trained on a Vietnamese-language dataset with the goal of improving Vietnamese language understanding and generation capabilities, while enhancing performance on tasks that require integrating information retrieved from external documents.

**Purpose of Use:**

The GRPO-VI-Qwen2-7B-RAG model is trained for RAG while retaining its conversational capability (with context length up to 8192 tokens). Therefore, it can handle the following scenarios:

* RAG-related tasks: multi-hop reasoning, negative filtering, information integration, and positive/negative identification.

* STEM tasks (related to mathematics and coding).

* General question answering.

**Training Methodology:**

The model is trained in two stages: Supervised Fine-Tuning and GRPO.

* Supervised Fine-Tuning Data:
Includes 10K RAG samples and 30K conversational samples covering math-related and general domain questions, all following a "think first, then answer" format.

* GRPO Data:
Consists of 10K RAG samples and 3K samples related to math and code.

* Reward Scoring:
Scores are assigned based on heuristics such as formatting quality, length of the reasoning section, length of the answer, purity of Vietnamese language in responses, string repetition, and a reward model that evaluates semantic quality for both RAG and STEM-related tasks.

**Limitations:**

The model may have the following limitations:

* It does not guarantee accuracy for questions related to politics, society, etc.

* It may exhibit bias or express inappropriate viewpoints.

**Benchmarks**

We evaluated several LLMs on the RAG task using a manually curated dataset created by our team: [EvalRAGData](https://huggingface.co/datasets/AITeamVN/EvalRAGData).

The evaluation was conducted by human annotators using a 10-point scoring scale.
Detailed results are as follows:
| Model                | Score |
|----------------------|------------|
| GRPO-VI-Qwen2-7B-RAG     | 9.24 | 
| Vi-Qwen2-7B-RAG     | 9.03 | 
| Vi-Qwen2-3B-RAG     | 8.65 | 
| Vi-Qwen2-1.5B-RAG     | 8.45 | 
| Qwen2.5-7B-Instruct     | 8.06 | 
| Llama3.1     | 7.55 | 
| Vistral 7B     | 6.62 | 
| Vi RAG GEMMA 2B     | 3.02 | 


In addition, we also conducted benchmarks on the VMLU leaderboard:
| Model                | Stem | Social Science | Humanities | Others  |  Average |
|----------------------|------------|------------|------------|-------------|--------------|
| GRPO_Qwen2_7B_RAG            | 62.11     | 60.86    | 52.8     | 51.56     | 57.4       | 
| Vi-Qwen2-7B-RAG            | 60.22     | 57.8    | 52.67     | 51.08     | 56.04       | 

**How to use:**

#### 1. Use for RAG

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
path = 'AITeamVN/GRPO-VI-Qwen2-7B-RAG'
model = AutoModelForCausalLM.from_pretrained(
    path,
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    use_cache=True
)
tokenizer = AutoTokenizer.from_pretrained(path)

system_prompt = """Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực. Hãy luôn trả lời một cách hữu ích nhất có thể.

Bạn hãy trả lời theo định dạng sau:
<think>
[Suy nghĩ, phân tích của bạn]
</think>
[Câu trả lời của bạn]
"""

template = '''Chú ý các yêu cầu sau:
- Câu trả lời phải chính xác và đầy đủ nếu ngữ cảnh có câu trả lời. 
- Chỉ sử dụng các thông tin có trong ngữ cảnh được cung cấp.
- Chỉ cần từ chối trả lời và không suy luận gì thêm nếu ngữ cảnh không có câu trả lời.
Hãy trả lời câu hỏi dựa trên ngữ cảnh:
### Ngữ cảnh :
{context}

### Câu hỏi :
{question}

### Trả lời :'''

context = '''- Ngữ cảnh 1: Những chỉ dấu sáng của xuất khẩu dệt may trong năm 2024 Là một trong 4 nhóm hàng đạt kim ngạch trên 1 tỷ USD trong tháng 1/2024, dệt may Việt Nam đã có khởi đầu thuận lợi trong chặng đường đua xuất khẩu. Theo số liệu của Cục Xuất nhập khẩu (Bộ Công Thương), chỉ số sản xuất của ngành dệt may tháng 1/2024 khá khả quan, trong đó dệt tăng 46,2%; sản xuất trang phục tăng 20,9%; sản phẩm vải dệt từ sợi tự nhiên tăng 57%; quần áo mặc thường tăng 25,8%... Dệt may cũng đứng vào top 4 ngành hàng đạt kim ngạch xuất khẩu trên 1 tỷ USD, đạt mức tăng trưởng 28,6% so với cùng kỳ năm 2023. Kết quả khả quan như trên được nhận định là nhờ sự phục hồi của các doanh nghiệp từ cuối năm 2023, khi đơn hàng dần tăng trở lại nhờ nhu cầu may mặc dịp lễ, Tết. Điển hình như Công ty CP Đầu tư và Thương mại TNG, hiện doanh nghiệp đã ký được những đơn hàng mới cho 6 tháng đầu năm 2024. Theo đó, TNG cũng đã lên kế hoạch doanh thu năm 2024 tăng từ 5 - 10% so với năm 2023. Còn với Tổng Công ty May 10, năm 2024, May 10 đặt mục tiêu doanh thu đạt 4.500 tỷ đồng, lợi nhuận đạt 130 tỷ đồng, thu nhập bình quân 9,5 triệu đồng/người/tháng. Thông tin từ Tập đoàn Dệt may Việt Nam, có những chỉ dấu sáng cho ngành dệt may hồi phục trở lại, nhất là tại những thị trường xuất khẩu truyền thống và lớn của ngành. Trong đó, Mỹ với tín hiệu có thể có 3 đợt cắt giảm lãi suất lên tới 0,75% là động lực thúc đẩy tiêu dùng trở lại. Bên cạnh đó, các quốc gia cạnh tranh gặp nhiều vấn đề về lao động, xung đột vũ trang ở trong nước, trong khi Việt Nam là một điểm đến an toàn cũng là một động lực mới cho đơn hàng có khả năng quay lại Việt Nam tốt hơn. Kinh tế vĩ mô trong nước tiếp tục ổn định, dự báo tăng trưởng GDP cao hơn 2023. Dù vậy, các chuyên gia vẫn khuyến cáo, bài học kinh nghiệm từ năm 2023 cho thấy thị trường thế giới hiện nay biến động rất khó lường, do vậy doanh nghiệp dệt may cần chuẩn bị tâm thế vững vàng, nội lực đủ mạnh để chớp nhanh cơ hội, cũng như nâng cao sức chống chịu.

- Ngữ cảnh 2: Dệt may Thành Công (TCM) đặt kế hoạch lợi nhuận năm 2024 tăng trưởng 21% Sau năm 2023 ghi nhận lợi nhuận giảm 52,4%, về 133,8 tỷ đồng, CTCP Dệt may - Đầu tư - Thương mại Thành Công (mã TCM - sàn HOSE) đã lên kế hoạch tăng trưởng trong năm 2024. Trong năm 2024, Công ty Dệt may Thành Công đặt kế hoạch kinh doanh với doanh thu thuần 3.707,4 tỷ đồng, tăng 12% so với cùng kỳ, lợi nhuận sau thuế dự kiến 161,23 tỷ đồng, tăng 21% so với thực hiện trong năm 2023. Về tình hình đơn hàng trong tháng 2/2024, Công ty Dệt may Thành Công cho biết đã nhận vượt kế hoạch doanh thu cho đơn hàng quý I/2024 và đã nhận khoảng 80% kế hoạch doanh thu cho đơn hàng quý II/2024. Theo dự báo tình hình xuất khẩu dệt may Việt Nam năm 2024 và theo tình hình tiếp nhận đơn hàng hiện tại của Công ty, Công ty hy vọng năm 2024 tình hình đơn hàng xuất khẩu sẽ khả quan hơn so với năm 2023. Ngoài ra, Công ty Dệt may Thành Công cũng cho biết hoạt động xuất khẩu hàng dệt may của Công ty được xuất khẩu sang các thị trường lớn trên thế giới . Trong đó, 74,9% lượng hàng được xuất sang thị trường châu Á (Nhật Bản chiếm 28,61%, Hàn Quốc chiếm 22,93%, Trung Quốc chiếm 9,99%, Việt Nam chiếm 6,58%); 20% được xuất khẩu sang thị trường Châu Mỹ (chủ yếu Mỹ, Canada) … và các thị trường khác như Châu Âu, thị trường Anh. Lợi nhuận Dệt may Thành Công lao dốc trong năm 2023 Xét về hoạt động kinh doanh trong quý IV/2023, Công ty Dệt may Thành Công ghi nhận doanh thu đạt 814,6 tỷ đồng, giảm 13,1% so với cùng kỳ, lợi nhuận sau thuế ghi nhận 22,36 tỷ đồng, giảm 62,6% so với thực hiện trong quý IV/2022. Trong đó, biên lợi nhuận gộp giảm từ 16,3%, về còn 15,9%. Lũy kế trong năm 2023, Công ty Dệt may Thành Công ghi nhận doanh thu đạt 3.324,82 tỷ đồng, giảm 23,3% so với cùng kỳ, lợi nhuận sau thuế ghi nhận 133,8 tỷ đồng, giảm 52,4% so với cùng kỳ năm trước. Trong năm 2023, Công ty Dệt may Thành Công đặt kế hoạch doanh thu 3.927,4 tỷ đồng, giảm 9% so với cùng kỳ và lợi nhuận trước thuế dự kiến 244,9 tỷ đồng, giảm 13% so với thực hiện trong năm 2022. Như vậy, kết thúc năm 2023 với lợi nhuận trước thuế đạt 188,8 tỷ đồng, Công ty Dệt may Thành Công chỉ hoàn thành 77,1% so với kế hoạch lãi 244,9 tỷ đồng trong năm 2023. Lý giải về kết quả kinh doanh lao dốc năm 2023, ông Trần Như Tùng, Chủ tịch HĐQT Công ty Dệt may Thành Công cho biết trong năm 2023 là một năm đầy khó khăn và thách thức của các doanh nghiệp ngành dệt may, tình hình sản xuất kinh doanh của Công ty cũng gặp không ít khó khăn và thử thách do tình hình kinh tế thế giới và Việt Nam không thuận lợi trong năm làm giảm nhu cầu tiêu thụ, doanh nghiệp thiếu đơn hàng dẫn đến kết quả kinh doanh không đạt kế hoạch đề ra. Đóng cửa phiên giao dịch ngày 8/3, cổ phiếu TCM đóng cửa giá tham chiếu 45.000 đồng/cổ phiếu.

- Ngữ cảnh 3: Dệt may TNG: Đơn hàng mới từ Walmart, H&M… có thể giúp lợi nhuận năm 2024 tăng tới 47% Với việc phát triển thành công loạt khách hàng lớn mới, bao gồm cả Walmart và H&M trong quý 3/2023, lợi nhuận của Dệt may TNG (mã cổ phiếu TNG) trong năm 2024 có thể tăng tới 47%. Vừa qua, Công ty Cổ phần Đầu tư và Thương mại TNG (Dệt may TNG, mã cổ phiếu TNG - sàn HNX) vừa cho biết, đến giữa tháng 12/2023, công ty đã hoàn thành 100% kế hoạch doanh thu cả năm 2023, tương ứng mức 6.800 tỷ đồng và về đích trước kế hoạch 16 ngày. Hiện Dệt may TNG dự kiến tổng doanh thu cả năm 2023 sẽ đạt 7.030 tỷ đồng, vượt 3% so với kế hoạch năm và tăng 4% so với cùng kỳ năm 2022. Theo mục tiêu đề ra tại Đại hội đồng cổ đông thường niên năm 2023, Dệt may TNG đặt mục tiêu doanh thu cả năm nay là 6.800 tỷ đồng và lợi nhuận 299 tỷ đồng, đều là các chỉ tiêu tài chính cao nhất trong lịch sử hoạt động của doanh nghiệp này. Tuy nhiên, chỉ tiêu lợi nhuận có thể khó hoàn thành khi lũy kế 9 tháng đầu năm nay, Dệt may TNG mới ghi nhận lãi 171 tỷ đồng - tương đương hơn 57% mục tiêu cả năm. Nguyên nhân chủ yếu do tình trạng thiếu đơn hàng nghiêm trọng của toàn ngành dệt may buộc Dệt may TNG phải nhận các đơn hàng có biên lợi nhuận thấp để duy trì sản xuất. Đồng thời, tổng cầu dệt may toàn cầu giảm khiến giá bán các sản phẩm may mặc giảm đáng kể. Theo đánh giá mới nhất của BSC Equity Research, Dệt may TNG hiện có triển vọng hồi phục tốt hơn các doanh nghiệp cùng ngành khi thị trường dệt may dần bước vào pha phục hồi trong giai đoạn 2024 - 2025 nhờ doanh nghiệp này đã duy trì được quy mô doanh thu trong giai đoạn khó khăn nhất. Trong khi đó, hầu hết các doanh nghiệp khác phải ghi nhận doanh thu giảm từ 20% - 50%. Do vậy, khi đơn giá/đơn hàng dần hồi phục trở lại theo nhu cầu của thị trường, biên lợi nhuận được cải thiện sẽ giúp Dệt may TNG tăng trưởng trở lại mạnh hơn các doanh nghiệp cùng ngành. Lợi nhuận năm 2024 của Dệt may TNG kỳ vọng có thể tăng tới 47% so với năm 2023, theo BSC Equity Research. Các thị trường xuất khẩu lớn nhất của doanh nghiệp dệt may này gồm: Mỹ (chiếm 40% tổng doanh thu), EU (chiếm 40%), còn lại là các thị trường khác như Nga, Canada, Hà Lan , Hàn Quốc... Trong đó, tồn kho quần áo tại Mỹ tính đến tháng 9/2023 đã giảm tháng thứ 10 liên tiếp, giảm 11% so với vùng đỉnh hồi cuối năm 2022, xuống tương đương hồi nửa đầu năm 2022. Theo BSC Equity Research, mức tồn kho của nhóm khách hàng chính của Dệt may TNG như Adidas, PUMA, Columbia Sportwear đã giảm về tiệm cận mức trung bình của những năm trước đó. Cụ thể, tồn kho của Adidas và của Puma hiện lần lượt chỉ còn 5,5 tỷ EUR và 1,9 tỷ EUR, tương đương hồi quý 2/2022. Riêng tồn kho của Columbia Sportwear đạt 1,1 tỷ USD, tăng 20% so với quý 3/2022 nhưng điều này không quá ảnh hưởng do Columbia Sportwear ghi nhận doanh số tăng trưởng mạnh tại loạt thị trường trọng điểm, như Canada (tăng 17% so với quý 3/2022), châu Á (tăng 18%), và châu Âu – Trung Đông - châu Phi (EMEA) (tăng 37%). Nhìn chung, hàng tồn kho được đánh giá sẽ tiếp tục giảm trong quý 4/2023 nhờ các đợt giảm giá cuối năm tại các thị trường Mỹ và châu Âu (Black Friday, Cyber Monday, Boxing day,...) và các nhãn hàng sẽ tái nhập trở lại trong giai đoạn đầu năm 2024 để phục vụ thị trường cho vụ Xuân - Hè. Ngoài ra, trong năm 2023, bên cạnh việc duy trì lượng đơn hàng đối với những khách hàng hiện hữu, Dệt may TNG còn phát triển thành công thêm một số khách hàng mới như Walmart , H&M, LIDL trong sản xuất nhiều mặt hàng như áo khoác, áo nỉ, áo bơi, quần legging,... Do đó, Dệt may TNG kỳ vọng sẽ ghi nhận được nguồn đơn tăng thêm từ những đối tác mới trên. Trong quý 3/2023, doanh nghiệp này đã vượt qua bài kiểm định của các nhãn hàng kể trên về cả chất lượng và công suất nhà máy. Đồng thời, Dệt may TNG cũng đã đáp ứng các yêu cầu về ESG của khách hàng như xây dựng lộ trình sử dụng 100% năng lượng tái tạo, nguyên liệu tái chế, giảm phát thải carbon, và đảm bảo chế độ cho người lao động.

- Ngữ cảnh 4: Sợi Thế Kỷ (mã: STK) cũng có kế hoạch doanh thu đạt 2.103 tỷ đồng, tăng 189% so với năm 2023 và lợi nhuận sau thuế đạt 300 tỷ đồng, tăng 342%. Cơ sở để doanh nghiệp này đặt mục tiêu kinh doanh cao trong năm 2024 đến từ việc sợi tái chế là động lực tăng trưởng chính và nhà máy Unitex mới bắt đầu đi vào hoạt động vào năm 2024 giúp thúc đẩy tăng trưởng doanh thu của STK trong dài hạn. Nhà máy sợi Unitex có công suất quy mô 60.000 tấn sợi/năm.

- Ngữ cảnh 5: Tổng Giám đốc CTCP Dệt may - Đầu tư - Thương mại Thành Công (mã: TCM) đã công bố kế hoạch kinh doanh năm 2024 với mục tiêu doanh thu thuần đạt 3.707 tỷ đồng, tăng 112% so với cùng kỳ năm 2023 và lợi nhuận sau thuế đạt 161 tỷ đồng, tăng 121% so với năm ngoái. Hiện dệt may TCM chưa công bố mục tiêu và nhiệm vụ cụ thể nhằm thực hiện hóa kế hoạch kinh doanh 2024. Tuy nhiên, theo báo cáo kinh doanh tháng 1/2024, TCM đã vượt kế hoạch doanh thu cho đơn hàng quý 1 và đã nhận khoảng 80% kế hoạch doanh thu cho đơn hàng quý 2/2024.'''

question = 'Các doanh nghiệp ngành dệt may nào đã công bố kế hoạch kinh doanh năm 2024 với mục tiêu tăng trưởng doanh thu vượt 100% so với năm 2023 và những yếu tố nào giúp họ đạt được mục tiêu này?'

conversation = [{"role": "system", "content": system_prompt }]
conversation.append({"role": "user", "content": template.format(context = context, question = question)})
text = tokenizer.apply_chat_template(
    conversation,
    tokenize=False,
    add_generation_prompt=True)
model_inputs = tokenizer(text,return_tensors="pt").to(model.device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=4096,
    temperature = 0.1,
    #top_p=0.95,
    #top_k=40,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)

'''
<think>
Trong ngữ cảnh 1, 2, 3, 4 và 5, có một số doanh nghiệp ngành dệt may đã công bố kế hoạch kinh doanh năm 2024 với mục tiêu tăng trưởng doanh thu vượt 100% so với năm 2023. Cụ thể:

- **Dệt may TNG (TNG.HNX)**: Mục tiêu doanh thu 6.800 tỷ đồng, tăng 4% so với cùng kỳ năm 2022, và lợi nhuận 299 tỷ đồng. Tuy nhiên, mục tiêu này không vượt 100% so với năm 2023. 

- **CTCP Dệt may - Đầu tư - Thương mại Thành Công (TCM.HOSE)**: Mục tiêu doanh thu 3.707 tỷ đồng, tăng 12% so với cùng kỳ, và lợi nhuận sau thuế 161 tỷ đồng, tăng 21% so với năm 2023. Mục tiêu này cũng không vượt 100%.

- **Sợi Thế Kỷ (STK.HNX)**: Mục tiêu doanh thu 2.103 tỷ đồng, tăng 189% so với năm 2023, và lợi nhuận sau thuế 300 tỷ đồng, tăng 342%. Đây là mục tiêu tăng trưởng vượt 100%.

- **Dệt may TNG (TNG.HNX)**: Mặc dù đã công bố mục tiêu, nhưng mục tiêu này không vượt 100%.

- **CTCP Dệt may - Đầu tư - Thương mại Thành Công (TCM.HOSE)**: Mục tiêu doanh thu 3.707 tỷ đồng, tăng 112% so với cùng kỳ, và lợi nhuận sau thuế 161 tỷ đồng, tăng 121% so với năm 2023. Đây là mục tiêu tăng trưởng vượt 100%.

Yếu tố giúp các doanh nghiệp đạt được mục tiêu này bao gồm:
1. **Đơn hàng mới từ các khách hàng lớn**: Dệt may TNG đã ký hợp đồng với Walmart và H&M, giúp tăng doanh thu và lợi nhuận.
2. **Phát triển thị trường mới**: Dệt may TNG đã mở rộng thị trường sang các thị trường mới như Mỹ, EU, Nga, Canada, Hà Lan, Hàn Quốc.
3. **Cải thiện biên lợi nhuận**: Dệt may TNG đang cố gắng cải thiện biên lợi nhuận bằng cách giảm tồn kho và tăng doanh số tại các thị trường trọng điểm.
4. **Năng lực sản xuất**: Nhà máy Unitex mới của Sợi Thế Kỷ có công suất 60.000 tấn sợi/năm, giúp tăng trưởng doanh thu trong dài hạn.
</think>
Dựa trên ngữ cảnh, có hai doanh nghiệp ngành dệt may đã công bố kế hoạch kinh doanh năm 2024 với mục tiêu tăng trưởng doanh thu vượt 100% so với năm 2023:

1. **CTCP Dệt may - Đầu tư - Thương mại Thành Công (TCM.HOSE)**:
   - **Mục tiêu doanh thu**: 3.707 tỷ đồng, tăng 112% so với cùng kỳ năm 2023.
   - **Lợi nhuận sau thuế**: 161 tỷ đồng, tăng 121% so với năm 2023.
   - **Yếu tố hỗ trợ**:
     - Đã vượt kế hoạch doanh thu cho đơn hàng quý 1 và nhận khoảng 80% kế hoạch doanh thu cho quý 2/2024.
     - Hoạt động xuất khẩu hàng dệt may sang các thị trường lớn như Nhật Bản, Hàn Quốc, Trung Quốc, và các thị trường khác.
     - Dự báo tình hình đơn hàng xuất khẩu khả quan hơn so với năm 2023.

2. **Sợi Thế Kỷ (STK.HNX)**:
   - **Mục tiêu doanh thu**: 2.103 tỷ đồng, tăng 189% so với năm 2023.
   - **Lợi nhuận sau thuế**: 300 tỷ đồng, tăng 342%.
   - **Yếu tố hỗ trợ**:
     - Sợi tái chế là động lực tăng trưởng chính.
     - Nhà máy Unitex mới bắt đầu đi vào hoạt động vào năm 2024, có công suất quy mô 60.000 tấn sợi/năm, giúp thúc đẩy tăng trưởng doanh thu trong dài hạn.

Cả hai doanh nghiệp đều đã đặt mục tiêu tăng trưởng cao và có những yếu tố cụ thể hỗ trợ để đạt được mục tiêu này, bao gồm việc ký kết đơn hàng mới, mở rộng thị trường, và đầu tư vào cơ sở hạ tầng sản xuất.
'''
```

#### 2. Math question

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
path = 'AITeamVN/GRPO-VI-Qwen2-7B-RAG'
model = AutoModelForCausalLM.from_pretrained(
    path,
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    use_cache=True
)
tokenizer = AutoTokenizer.from_pretrained(path)

system_prompt = """Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực. Hãy luôn trả lời một cách hữu ích nhất có thể.

Bạn hãy trả lời theo định dạng sau:
<think>
[Suy nghĩ, phân tích của bạn]
</think>
[Câu trả lời của bạn]
"""
prompt = "Giải phương trình sau: 2x^2 - 3x + 1 = 0"

conversation = [{"role": "system", "content": system_prompt }]
conversation.append({"role": "user", "content": prompt})
text = tokenizer.apply_chat_template(
    conversation,
    tokenize=False,
    add_generation_prompt=True)
model_inputs = tokenizer(text,return_tensors="pt").to(model.device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=4096,
    temperature = 0.1,
    #top_p=0.95,
    #top_k=40,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)


'''
<think>
Được, hãy giải phương trình bậc hai này: 2x^2 - 3x + 1 = 0. Phương trình bậc hai cơ bản có dạng ax^2 + bx + c = 0, và ở đây, a là 2, b là -3, và c là 1. Tôi nhớ rằng có một công thức tuyệt vời để giải các phương trình như thế này, gọi là công thức nghiệm bậc hai. Công thức đó là x = [-b ± sqrt(b^2 - 4ac)] / (2a). Hãy thay các số vào.

Đầu tiên, tôi cần tính biệt thức, đó là phần b^2 - 4ac. Vậy, hãy làm: (-3)^2 cho ta 9, và 4 lần 2 lần 1 là 8. Trừ đi, ta được 9 - 8, tức là 1. À, biệt thức là 1, điều này thật tuyệt vì nó là một số dương hoàn hảo, nghĩa là chúng ta sẽ có hai nghiệm thực và khác nhau.

Bây giờ, hãy tìm các nghiệm bằng công thức. Đầu tiên, tôi sẽ tính phần cộng: x = [3 + sqrt(1)] / 4. Điều này đơn giản hóa thành (3 + 1) / 4, tức là 4/4, bằng 1. Được, vậy là đã có một nghiệm.

Tiếp theo, phần trừ: x = [3 - sqrt(1)] / 4. Điều này trở thành (3 - 1) / 4, tức là 2/4, rút gọn lại là 1/2. Tuyệt, vậy là đã có cả hai nghiệm: x = 1 và x = 1/2.

Hãy kiểm tra nhanh bằng cách thay các nghiệm này vào phương trình gốc. Đối với x = 1, thay vào ta được 2(1)^2 - 3(1) + 1 = 2 - 3 + 1 = 0. Hoàn hảo! Và đối với x = 1/2, thay vào ta được 2(1/2)^2 - 3(1/2) + 1 = 2(1/4) - 3/2 + 1 = 1/2 - 3/2 + 1 = 0. Đúng rồi, mọi thứ đều khớp!

Vậy, các nghiệm của phương trình 2x^2 - 3x + 1 = 0 là x = 1 và x = 1/2. Mọi thứ đều đúng!
</think>
Phương trình bậc hai \(2x^2 - 3x + 1 = 0\) có các nghiệm là \(x = 1\) và \(x = \frac{1}{2}\). Các nghiệm này được tìm bằng công thức nghiệm bậc hai, và chúng đã được xác nhận bằng cách thay chúng trở lại vào phương trình ban đầu, cho kết quả bằng không.'''
```

#### 3. General Domain

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
path = 'AITeamVN/GRPO-VI-Qwen2-7B-RAG'
model = AutoModelForCausalLM.from_pretrained(
    path,
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    use_cache=True
)
tokenizer = AutoTokenizer.from_pretrained(path)

system_prompt = """Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực. Hãy luôn trả lời một cách hữu ích nhất có thể.

Bạn hãy trả lời theo định dạng sau:
<think>
[Suy nghĩ, phân tích của bạn]
</think>
[Câu trả lời của bạn]
"""
prompt = "Đỉnh núi cao nhất Việt Nam là gì?"

conversation = [{"role": "system", "content": system_prompt }]
conversation.append({"role": "user", "content": prompt})
text = tokenizer.apply_chat_template(
    conversation,
    tokenize=False,
    add_generation_prompt=True)
model_inputs = tokenizer(text,return_tensors="pt").to(model.device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=4096,
    temperature = 0.1,
    #top_p=0.95,
    #top_k=40,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)


'''
<think>
Được, vậy hãy nghĩ về đỉnh núi cao nhất ở Việt Nam. Tôi biết rằng Việt Nam nằm ở Đông Nam Á, và nó có một dãy núi chạy dọc theo biên giới với Trung Quốc. Dãy núi này được gọi là Dãy Trường Sơn. Tôi nhớ đã nghe nói rằng đây là nơi có một số đỉnh núi rất cao.

Bây giờ, nếu tôi muốn xác định đỉnh núi nào là cao nhất, tôi nên tìm hiểu thêm về địa hình ở đó. À, phải rồi! Có một đỉnh núi nổi tiếng gọi là Fansipan. Tôi đã nghe nhiều về nó; nó thường được nhắc đến khi nói về điểm cao nhất của Việt Nam.

Hãy kiểm tra lại điều này. Tôi nhớ đã đọc ở đâu đó rằng Fansipan có độ cao khoảng 3.143 mét. Đó là khá cao, nhưng để chắc chắn, tôi nên so sánh nó với các đỉnh núi khác trong khu vực.

À, chờ đã, còn có một số đỉnh núi khác như Đỉnh Bạch Mã và Đỉnh Lũng Cú. Nhưng tôi khá chắc chắn rằng Fansipan vẫn là đỉnh núi cao nhất. Nó được công nhận rộng rãi là đỉnh núi cao nhất của Việt Nam.

Vậy, sau khi suy nghĩ kỹ, tôi tự tin rằng Fansipan chính là đỉnh núi cao nhất ở Việt Nam. Độ cao và vị trí của nó khiến nó trở thành điểm cao nhất của cả nước. Điều này phù hợp với những gì tôi đã học từ các nguồn địa lý đáng tin cậy.
</think>
Đỉnh núi cao nhất ở Việt Nam là Fansipan, nằm trong dãy núi Hoàng Liên Sơn ở vùng Tây Bắc. Fansipan có độ cao khoảng 3.143 mét (10.312 feet) so với mực nước biển, khiến nó trở thành điểm cao nhất của cả nước. Đỉnh núi này không chỉ là biểu tượng của địa lý Việt Nam mà còn thu hút nhiều du khách và người leo núi vì vẻ đẹp tự nhiên và thách thức về mặt thể chất.```
'''

```
**Developer**

Member: Nguyen Nho Trung, Nguyen Van Huy, Nguyễn Nhat Quang

## Contact

**Email**: nguyennhotrung3004@gmail.com


## Citation

```Plaintext
@misc{ViRAG-Gen,
  title={ViRAG-Gen-v2: A GRPO-Based Specialized LLM for Vietnamese Retrieval-Augmented Generation.}},
  author={Nguyen Nho Trung, Nguyen Van Huy, Nguyen Nhat Quang},
  year={2025},
  publisher={Huggingface},
} 
```
