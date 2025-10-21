---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
- hi
tags:
- synthetic
- personas
- NVIDIA
- Hindi
- Devanagari
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: en_IN
    path: data/en_IN-*
  - split: hi_Deva_IN
    path: data/hi_Deva_IN-*
  - split: hi_Latn_IN
    path: data/hi_Latn_IN-*
dataset_info:
  features:
  - name: uuid
    dtype: string
  - name: professional_persona
    dtype: string
  - name: linguistic_persona
    dtype: string
  - name: sports_persona
    dtype: string
  - name: arts_persona
    dtype: string
  - name: travel_persona
    dtype: string
  - name: culinary_persona
    dtype: string
  - name: persona
    dtype: string
  - name: cultural_background
    dtype: string
  - name: linguistic_background
    dtype: string
  - name: skills_and_expertise
    dtype: string
  - name: skills_and_expertise_list
    dtype: string
  - name: hobbies_and_interests
    dtype: string
  - name: hobbies_and_interests_list
    dtype: string
  - name: career_goals_and_ambitions
    dtype: string
  - name: sex
    dtype: string
  - name: age
    dtype: int64
  - name: marital_status
    dtype: string
  - name: education_level
    dtype: string
  - name: education_degree
    dtype: string
  - name: occupation
    dtype: string
  - name: first_language
    dtype: string
  - name: second_language
    dtype: string
  - name: third_language
    dtype: string
  - name: zone
    dtype: string
  - name: state
    dtype: string
  - name: district
    dtype: string
  - name: country
    dtype: string
  splits:
  - name: en_IN
    num_bytes: 5183912347
    num_examples: 1000000
  - name: hi_Deva_IN
    num_bytes: 12567786108
    num_examples: 1000000
  - name: hi_Latn_IN
    num_bytes: 5564242261
    num_examples: 1000000
  download_size: 9594315340
  dataset_size: 23315940716
---

Nemotron-Personas-India
=========================================================================
<center>
  <img src="images/nemotron_personas_india_approach.png" alt="Nemotron-Personas-India" width="400px">
  <p>
    <em>A compound AI approach to personas grounded in real-world distributions</em><br>
    <em>वास्तविक दुनिया के वितरण पर आधारित व्यक्तित्वों के लिए एक मिश्रित AI दृष्टिकोण</em>
  </p>
</center>

# Dataset Overview (डेटासेट अवलोकन)
Nemotron-Personas-India is an open-source (CC BY 4.0) dataset of synthetically-generated personas. This dataset is grounded in real-world demographic, geographic and personality trait distributions in India to capture the diversity and richness of the Indian population. It is a variant of [Nemotron-Personas](https://huggingface.co/datasets/nvidia/Nemotron-Personas), and the first Indic dataset of its kind aligned with statistics for names, sex, age, religion, spoken languages, background, marital status, education and occupation among other attributes. This version of the dataset provides high-quality personas for a variety of modeling use-cases in both English and Hindi (Devanagari and Latin scripts).

Nemotron-Personas-India supports Indian model builders in developing [Sovereign AI](https://www.nvidia.com/en-us/lp/industries/global-public-sector/sovereign-ai-technical-overview/) systems that incorporate important region-specific demographics and cultural context. The dataset improves diversity of synthetically-generated data, mitigates biases, and prevents [model collapse](https://medium.com/data-science/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai-7cd380208d14) (degradation caused by uncurated training on another model’s outputs) by reflecting India’s real geographic and demographic distributions. In particular, the dataset is designed to be more representative of underlying demographic distributions along multiple axes, including age (e.g. older personas), geography (e.g., rural personas), spoken languages, education, occupation, religious identities, etc., as compared to other persona datasets. As an example, one can produce high-quality, multi-turn chat conversation data with real names, ages, occupation, cultural and education backgrounds, all of which bring unique perspectives and angles to that data.

Produced using [NeMo Data Designer](https://docs.nvidia.com/nemo/microservices/latest/generate-synthetic-data/index.html), an enterprise-grade compound AI system for synthetic data generation, the dataset leverages a proprietary Probabilistic Graphical Model (PGM) along with an Apache-2.0-licensed GPT-OSS-120B model and an ever-expanding set of validators and evaluators built into Data Designer. An extended version of Nemotron-Personas-India will be soon available for use in NeMo Data Designer itself.

This dataset is ready for commercial use.

Nemotron-Personas-India सिंथेटिक रूप से जेनरेट किए गए पर्सोना का एक ओपन-सोर्स (CC BY 4.0) डेटासेट है। यह डेटासेट भारतीय आबादी की विविधता और समृद्धि को दर्शाने के लिए भारत में वास्तविक जनसांख्यिकीय, भौगोलिक और व्यक्तित्व विशेषताओं के वितरण पर आधारित है। यह [Nemotron-Personas](https://huggingface.co/datasets/nvidia/Nemotron-Personas) का एक संस्करण है और अपनी तरह का पहला भारतीय डेटासेट है जो नाम, लिंग, आयु, धर्म, बोली जाने वाली भाषाओं, पृष्ठभूमि, वैवाहिक स्थिति, शिक्षा और व्यवसाय जैसी विशेषताओं के आँकड़ों के अनुरूप है। यह संस्करण विभिन्न प्रकार के मॉडलिंग यूज़-केस के लिए अंग्रेज़ी और हिंदी (देवनागरी और लैटिन लिपियों) दोनों में उच्च-गुणवत्ता वाले पर्सोना प्रदान करता है।

Nemotron-Personas-India भारतीय मॉडल निर्माताओं को ऐसे [सॉवरेन AI सिस्टम](https://www.nvidia.com/en-us/lp/industries/global-public-sector/sovereign-ai-technical-overview/) विकसित करने में सहायता करता है जो महत्वपूर्ण क्षेत्र-विशिष्ट जनसांख्यिकी और सांस्कृतिक संदर्भ को शामिल करते हैं। यह डेटासेट भारत के वास्तविक भौगोलिक और जनसांख्यिकीय वितरण को दर्शाकर सिंथेटिक डेटा की विविधता में सुधार करता है, पूर्वाग्रहों को कम करता है, और [मॉडल कोलैप्स](https://medium.com/data-science/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai-7cd380208d14) (दूसरे मॉडल के आउटपुट पर बिना जाँचे-परखे प्रशिक्षण के कारण होने वाली गिरावट) को रोकता है। विशेष रूप से, अन्य पर्सोना डेटासेट की तुलना में, इस डेटासेट को कई पैमानों पर अंतर्निहित जनसांख्यिकीय वितरण का अधिक प्रतिनिधित्व करने के लिए डिज़ाइन किया गया है, जिसमें आयु (जैसे, अधिक उम्र वाले पर्सोना), भूगोल (जैसे, ग्रामीण पर्सोना), बोली जाने वाली भाषाएँ, शिक्षा, व्यवसाय, और धार्मिक पहचान आदि शामिल हैं। उदाहरण के लिए, इसके उपयोग से वास्तविक नाम, आयु, व्यवसाय, सांस्कृतिक और शैक्षिक पृष्ठभूमि के साथ उच्च-गुणवत्ता वाला मल्टी-टर्न चैट वार्तालाप डेटा बनाया जा सकता है, जो उस डेटा में अद्वितीय दृष्टिकोण और पहलू लाते हैं।

सिंथेटिक डेटा जेनरेशन के लिए एक एंटरप्राइज-ग्रेड कंपाउंड AI सिस्टम, [NeMo Data Designer](https://docs.nvidia.com/nemo/microservices/latest/generate-synthetic-data/index.html), का उपयोग करके निर्मित यह डेटासेट एक प्रोप्राइटरी प्रोबेबिलिस्टिक ग्राफिकल मॉडल (PGM), Apache-2.0-लाइसेंस वाले GPT-OSS-120B मॉडल, और Data Designer में निर्मित वैलिडेटर्स और इवैल्यूएटर्स के लगातार बढ़ते सेट का लाभ उठाता है। Nemotron-Personas-India का एक विस्तारित संस्करण जल्द ही NeMo Data Designer में उपयोग के लिए उपलब्ध होगा।
यह डेटासेट व्यावसायिक उपयोग के लिए तैयार है।

यह डेटासेट व्यावसायिक उपयोग के लिए तैयार है।

## What is NOT in the dataset (डेटासेट में क्या नहीं है)
Given the emphasis on personas, the dataset excludes other fields available in NeMo Data Designer, e.g., first/last names, religion, and synthetic addresses. Also excluded are personas generally of relevance to enterprise clients (e.g., religious, finance, healthcare). Please [reach out](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/contact-sales/) to explore enterprise use-cases.

All data, while mirroring real-world distributions, is completely artificially generated. Any similarity in names or persona descriptions to actual persons, living or dead, is purely coincidental.

पर्सोना पर विशेष ध्यान देने के कारण, इस डेटासेट में NeMo Data Designer में उपलब्ध अन्य फ़ील्ड, जैसे पहला/अंतिम नाम, धर्म और सिंथेटिक पते, शामिल नहीं किए गए हैं। इसमें ऐसे पर्सोना भी शामिल नहीं हैं जो आम तौर पर एंटरप्राइज़ ग्राहकों के लिए प्रासंगिक होते हैं (जैसे धार्मिक, वित्त, स्वास्थ्य सेवा)। एंटरप्राइज़ यूज़-केस के बारे में जानने के लिए कृपया [संपर्क करें](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/contact-sales/)।

यह पूरा डेटा, भले ही वास्तविक दुनिया के वितरण को दर्शाता है, लेकिन यह पूरी तरह से कृत्रिम रूप से बनाया गया है। नामों या पर्सोना-विवरण की किसी भी वास्तविक व्यक्ति (जीवित या मृत) से कोई भी समानता पूरी तरह से एक संयोग है।


# Data Developer (डेटा डेवलपर)
NVIDIA Corporation

# Release Date (रिलीज़ दिनांक)
Hugging Face 10/13/2025 via https://huggingface.co/datasets/nvidia/Nemotron-Personas-India

# Dataset Creation Date (डेटासेट निर्माण दिनांक)
10/10/2025

# License/Terms of Use (निबंधन एवं शर्तें)
This dataset is licensed under the Creative Commons Attribution 4.0 International License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).
यह डेटासेट क्रिएटिव कॉमन्स एट्रिब्यूशन 4.0 इंटरनेशनल लाइसेंस (CC BY 4.0) के तहत लाइसेंसशुदा है।

# Use Case (उपयोग)
Developers working on Sovereign AI, training LLMs, and/or looking to improve diversity of synthetically generated data, mitigate data/model biases, and prevent model collapse.

सॉवरेन AI पर काम करने वाले, LLMs को प्रशिक्षित करने वाले, और/या ऐसे डेवलपर्स जो सिंथेटिक रूप से जेनरेट किए गए डेटा की विविधता में सुधार करना, डेटा/मॉडल के पूर्वाग्रहों को कम करना, और मॉडल कोलैप्स को रोकना चाहते हैं।

# Data Version (डेटा संस्करण)
1.0 (10/13/2025)

# Intended Use (निर्धारित उपयोग)
The Nemotron-Personas-India dataset is intended to be used by the community to continue to improve open models and push the state of the art. The data may be freely used to train any model. We welcome feedback from the open-source community and invite developers, researchers, and data enthusiasts to explore the dataset and build upon it.

The Nemotron-Personas-India dataset is grounded in distributions of self-reported demographic data from the 2011 census of India. As such, its primary goal is to support Sovereign AI development by combating missing data and/or potential biases present in model training data today, especially when it comes to existing persona datasets used in synthetic data generation. Despite the improved data diversity and fidelity to India’s population, we are still limited by data availability, current staleness of data, and reasonable model complexity. This results in some necessary independence assumptions; for instance, that occupations are independent of education degree, given the district, age and sex. The census report provides statistics for only 26 broad occupation categories. We expand on these categories using the National Classification of Occupations-2004 to ~3000 detailed occupations. The statistics for transitioning from the broad categories to detailed occupations is done with the aid of an LLM. We leave further efforts to improve fidelity to future work.

Nemotron-Personas-India डेटासेट को समुदाय के उपयोग के लिए बनाया गया है, ताकि ओपन मॉडल्स को लगातार बेहतर बनाया जा सके और इस क्षेत्र में नई प्रगति की जा सके। इस डेटा का उपयोग किसी भी मॉडल को प्रशिक्षित करने के लिए स्वतंत्र रूप से किया जा सकता है। हम ओपन-सोर्स समुदाय से मिलने वाले फीडबैक का स्वागत करते हैं और डेवलपर्स, शोधकर्ताओं और डेटा के प्रति उत्साही लोगों को इस डेटासेट को एक्सप्लोर करने और इसका विस्तार करने के लिए आमंत्रित करते हैं।
यह डेटासेट, भारत की 2011 की जनगणना से मिले स्व-रिपोर्ट किए गए जनसांख्यिकीय डेटा के वितरण पर आधारित है। इसलिए, इसका मुख्य लक्ष्य सॉवरेन AI के विकास में सहायता करना है। यह आज मॉडल प्रशिक्षण डेटा में मौजूद संभावित पूर्वाग्रहों और लुप्त डेटा की समस्या से निपटने में मदद करता है, विशेष रूप से सिंथेटिक डेटा बनाने के लिए उपयोग किए जाने वाले मौजूदा पर्सोना डेटासेट के संबंध में। भारत की आबादी के हिसाब से डेटा की बेहतर विविधता और सटीकता के बावजूद, हम अभी भी डेटा की उपलब्धता, डेटा के मौजूदा पुरानेपन, और मॉडल की उचित जटिलता जैसी सीमाओं से बंधे हैं। इसके परिणामस्वरूप, हमें कुछ आवश्यक स्वतंत्रता की धारणाएँ बनानी पड़ती हैं; उदाहरण के लिए, यह मानना कि किसी जिले, उम्र और लिंग को देखते हुए, व्यवसाय शिक्षा की डिग्री से स्वतंत्र हैं। जनगणना रिपोर्ट केवल 26 मुख्य व्यावसायिक श्रेणियों के लिए आँकड़े प्रदान करती है। हमने राष्ट्रीय व्यावसायिक वर्गीकरण-2004 का उपयोग करके इन श्रेणियों का विस्तार लगभग 3000 विस्तृत व्यवसायों तक किया है। मुख्य श्रेणियों से विस्तृत व्यवसायों में संक्रमण के आँकड़े एक LLM की सहायता से तैयार किए गए हैं। हम सटीकता में सुधार के आगे के प्रयासों को भविष्य के काम के लिए छोड़ते हैं।


# Dataset Details (डेटासेट का विवरण)

The dataset contains:
* 3M records total, with 1M in Hindi (Devanagari), 1M in Hindi (Latin), and 1M in English
* 21M persona descriptions total, with 7 personas/record within each language/script
* 27 fields excluding the UUID: 7 persona fields (each in English, Hindi and transliterated Hindi), and 20 contextual fields grounded in official demographic and labor statistics
* ~7.7B tokens total, including ~2.9B persona tokens 
* Comprehensive coverage across demographic, geographic, and personality trait axes
* ~560k unique names 
* 2,900+ occupation titles reflecting India’s workforce taken from the National Classification of Occupations - 2004.
* A variety of persona types: professional, linguistic, sports, arts, travel, culinary.
* Natural language persona attributes: cultural background, skills & expertise, goals & ambitions, hobbies & interests.

Nemotron-Personas-India was designed to align with India’s official demographic and labor statistics, while extending them into areas important for AI training. In practice, this meant:
* Occupations: We augment occupation statistics with finer-grained categories from the National Classification of Occupations-2004
* Translated categories: To ensure the full set of fields is available in both English and Hindi, we generated all fields in Devanagari and Latin scripts, all while maintaining consistency between English/Devangari/Latin.
* New states: The state of Telangana was formed in 2014, after the 2011 census report was made. Here, we retraced back the districts from Andhra Pradesh which formed Telangana and separated the statistics of both states using their constituent districts.
* Extrapolating naming conventions: The name distribution for the states Lakshadweep and Chhattisgarh was not available. Here, we estimated the distributions by interpolating the probability distributions of the states that share the closest match in terms of mother-tongues. This is based on the influence a mother-tongue can have over a person’s name.

These extensions build on a strong foundation of public data, helping create personas that are both statistically grounded and culturally representative, while remaining synthetic, privacy-preserving, and open.

इस डेटासेट में शामिल हैं:
* कुल 30 लाख रिकॉर्ड, जिनमें 10 लाख हिंदी (देवनागरी), 10 लाख हिंदी (लैटिन), और 10 लाख अंग्रेज़ी में हैं।
* कुल 2.1 करोड़ पर्सोना विवरण, और हर भाषा/लिपि में प्रति रिकॉर्ड 80 लाख पर्सोना हैं।
* UUID को छोड़कर 27 फ़ील्ड: 7 पर्सोना फ़ील्ड (प्रत्येक अंग्रेज़ी, हिंदी और लिप्यंतरित हिंदी में), और 20 प्रासंगिक फ़ील्ड जो आधिकारिक जनसांख्यिकीय और श्रम आँकड़ों पर आधारित हैं।
* कुल लगभग 770 करोड़ टोकन, जिनमें लगभग 290 करोड़ पर्सोना टोकन शामिल हैं।
* जनसांख्यिकीय, भौगोलिक और व्यक्तित्व विशेषताओं जैसे कई पहलुओं का व्यापक कवरेज।
* लगभग 5.5 लाख अनोखे नाम।
* 2,900 से ज़्यादा व्यवसायों के नाम, जिन्हें राष्ट्रीय व्यावसायिक वर्गीकरण - 2004 से लिया गया है और जो भारत के कार्यबल को दर्शाते हैं।
* कई तरह के पर्सोना: व्यावसायिक, भाषाई, खेल, कला, यात्रा, और खान-पान संबंधी।
* प्राकृतिक भाषा में पर्सोना की विशेषताएँ: सांस्कृतिक पृष्ठभूमि, कौशल और विशेषज्ञता, लक्ष्य और महत्वाकांक्षाएँ, और शौक और रुचियाँ।


Nemotron-Personas-India को भारत के आधिकारिक जनसांख्यिकीय और श्रम आँकड़ों के अनुरूप बनाया गया है, और साथ ही AI प्रशिक्षण के लिए महत्वपूर्ण क्षेत्रों तक इसका विस्तार भी किया गया है। इसके लिए हमने निम्नलिखित काम किए हैं:
* व्यवसाय: हमने राष्ट्रीय व्यावसायिक वर्गीकरण-2004 से और भी विस्तृत श्रेणियाँ लेकर व्यावसायिक आँकड़ों को बेहतर बनाया है।
* अनुवादित श्रेणियाँ: यह सुनिश्चित करने के लिए कि सभी फ़ील्ड अंग्रेज़ी और हिंदी दोनों में उपलब्ध हों, हमने सभी फ़ील्ड को देवनागरी और लैटिन लिपियों में तैयार किया, और इस दौरान अंग्रेज़ी/देवनागरी/लैटिन के बीच एकरूपता बनाए रखी।
* नए राज्य: तेलंगाना राज्य का गठन 2014 में, यानी 2011 की जनगणना रिपोर्ट के बाद हुआ था। इसलिए, हमने आंध्र प्रदेश के उन जिलों का पता लगाया जिनसे तेलंगाना बना और फिर उन जिलों के आधार पर दोनों राज्यों के आँकड़ों को अलग-अलग किया।
* नामकरण परंपराओं का अनुमान: लक्षद्वीप और छत्तीसगढ़ राज्यों के लिए नामों का वितरण उपलब्ध नहीं था। इसलिए, हमने उन राज्यों के आँकड़ों का उपयोग करके अनुमान लगाया जिनकी मातृभाषाएँ इन दोनों से सबसे ज़्यादा मेल खाती हैं। यह इस तथ्य पर आधारित है कि किसी व्यक्ति के नाम पर उसकी मातृभाषा का गहरा प्रभाव पड़ सकता है।


ये सभी विस्तार सार्वजनिक डेटा की एक मज़बूत नींव पर बनाए गए हैं। ये ऐसे पर्सोना बनाने में मदद करते हैं जो सांख्यिकीय रूप से सटीक होने के साथ-साथ सांस्कृतिक रूप से भी प्रातिनिधिक हैं, और साथ ही ये सिंथेटिक, गोपनीयता-संरक्षित और ओपन भी रहते हैं।

## Seed Data (स्रोत डेटा)
In order to capture the socio-demographic and geographic diversity and complexity of India’s population, Nemotron-Personas-India leveraged the following resources:
* [2011 census of India](https://censusindia.gov.in) published by the Registrar General and Census Commissioner of India
Indic name distribution data obtained from [Parsed Indian Electoral Rolls](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MUEGDT) provided by [Harvard Dataverse](https://dataverse.harvard.edu/) and [Gaurav Sood](https://dataverse.harvard.edu/dataverse/soodoku).

भारत की आबादी की सामाजिक, जनसांख्यिकीय और भौगोलिक विविधता और जटिलता को दर्शाने के लिए, Nemotron-Personas-India ने निम्नलिखित स्रोतों का उपयोग किया:
* भारत के रजिस्ट्रार जनरल और जनगणना आयुक्त द्वारा प्रकाशित [भारत की 2011 की जनगणना](https://censusindia.gov.in)।
* [हार्वर्ड डेटावर्स](https://dataverse.harvard.edu/) और [गौरव सूद](https://dataverse.harvard.edu/dataverse/soodoku) द्वारा प्रदान की गई [विश्लेषित भारतीय मतदाता सूचियों](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MUEGDT) से प्राप्त भारतीय नामों का वितरण डेटा।

## Schema (संरचना)
The dataset includes 27 fields: 7 persona fields and 20 contextual fields shown below. Researchers will find many contextual fields useful in zoning in on specific personas, which is challenging to do with existing datasets.
<center>
  <img src="images/nemotron_personas_india_schema_en.png" width="700px">
</center>

इस डेटासेट में नीचे बताए गए 27 फ़ील्ड शामिल हैं: 7 पर्सोना फ़ील्ड और 20 प्रासंगिक फ़ील्ड। शोधकर्ताओं के लिए, कई प्रासंगिक फ़ील्ड खास तरह के पर्सोना पर ध्यान केंद्रित करने में उपयोगी साबित होंगे। मौजूदा डेटासेट के साथ ऐसा करना एक मुश्किल काम है।
<center>
  <img src="images/nemotron_personas_india_schema_hi.png" width="700px">
</center>

## Field & Token Counts (फ़ील्ड और टोकन संख्या)
7.7B tokens (2.9B persona tokens) across 3M records in three scripts (English, Hindi Devanagari, Hindi Latin) and 27 columns, excluding the globally unique identifier. Note that data covers all 36 states and union territories of India as well as 640 districts.

तीन लिपियों (अंग्रेज़ी, हिंदी देवनागरी और हिंदी लैटिन) और 27 कॉलम में 30 लाख रिकॉर्ड में कुल 770 करोड़ टोकन (290 करोड़ पर्सोना टोकन सहित) हैं, इसमें विश्व स्तर पर अद्वितीय पहचानकर्ता शामिल नहीं है। ध्यान दें कि इस डेटा में भारत के सभी 36 राज्यों और केंद्र-शासित प्रदेशों के साथ-साथ 640 जिले भी शामिल हैं।

<center>
  <img src="images/nemotron_personas_india_field_stats.png" width="500px">
</center>

# Dataset Description & Quality Assessment (डेटासेट विवरण एवं गुणवत्ता मूल्यांकन)
The analysis below provides a breakdown across various axes of the dataset to emphasize the built-in diversity and pattern complexity of data.

नीचे दिया गया विश्लेषण, डेटा में मौजूद विविधता और पैटर्न की जटिलता पर ज़ोर देने के लिए, डेटासेट के विभिन्न पहलुओं का विवरण देता है।

## Names (नाम)
Since the focus of this dataset is on personas, names aren’t provided as dedicated fields. However, infused into persona-generation are 231,685 unique first names and 177,705 unique last names obtained from [Parsed Indian Electoral Rolls](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MUEGDT) provided by [Harvard Dataverse](https://dataverse.harvard.edu/) and [Gaurav Sood](https://dataverse.harvard.edu/dataverse/soodoku). We omit the use of a middle name owing to the complexity in acquiring reliable distributions for this.

चूंकि इस डेटासेट का मुख्य फोकस पर्सोना पर है, इसलिए इसमें नामों के लिए अलग से कोई फ़ील्ड नहीं है। हालांकि, पर्सोना बनाते समय इसमें [हार्वर्ड डेटावर्स](https://dataverse.harvard.edu/) और [गौरव सूद](https://dataverse.harvard.edu/dataverse/soodoku) द्वारा प्रदान की गई '[विश्लेषित भारतीय मतदाता सूचियों](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MUEGDT)' से प्राप्त 231,685 अनोखे फर्स्ट नेम और 177,705 अनोखे लास्ट नेम शामिल किए गए हैं। हमने मध्य नाम (middle name) का उपयोग नहीं किया है, क्योंकि इसके लिए भरोसेमंद आँकड़े पाना मुश्किल था।

## Age Distribution (आयु वितरण)
The age distribution of our Indian personas mirrors the country’s real demographic structure as of 2011, characterized by a large proportion of young adults. The total population majorly consists of people living in rural areas rather than in urban areas.

Note that minors under 18 are excluded from this dataset.

हमारे भारतीय पर्सोना की आयु का वितरण, देश की 2011 की वास्तविक जनसांख्यिकीय संरचना को दर्शाता है, जिसमें युवा वयस्कों का अनुपात बहुत बड़ा है। कुल आबादी में ज़्यादातर लोग शहरी इलाकों के बजाय ग्रामीण इलाकों में रहते हैं।

ध्यान दें कि 18 साल से कम उम्र के नाबालिगों को इस डेटासेट से बाहर रखा गया है।
<center>
  <img src="images/nemotron_personas_india_age_group_distribution.png" width="600px">
</center>

## Marital Status by Age Group (वैवाहिक स्थिति और आयु वर्ग)
The heatmap below displays the fraction of people for each age cohort who are (1) never married, (2) currently married, (3) widowed, (4) separated, or (5) Divorced. It highlights how marital status shifts over the life course in India, with “never married” dominating until only the early 20s, while “currently married” shoots up from the mid 20s to the early 30s, “separated” and “divorced” being flat, and “widowed” being much more pronounced in later life stages. The trends remain the same in both rural and urban regions. All of these considerations are of relevance to informing life experiences and personas in India.

नीचे दिया गया चित्र हर आयु वर्ग में लोगों के उस अनुपात को दिखाता है जो (1) अविवाहित हैं, (2) वर्तमान में विवाहित हैं, (3) विधवा/विधुर हैं, (4) अलग रह रहे हैं, या (5) तलाकशुदा हैं। यह दिखाता है कि भारत में जीवन के अलग-अलग पड़ावों पर वैवाहिक स्थिति कैसे बदलती है, जिसमें 'अविवाहित' श्रेणी 20-22 साल की उम्र तक हावी रहती है, जबकि 'वर्तमान में विवाहित' की संख्या 25 से 32-33 साल की उम्र में तेज़ी से बढ़ती है। 'अलग रह रहे' और 'तलाकशुदा' की संख्या लगभग स्थिर रहती है, और 'विधवा/विधुर' श्रेणी जीवन के बाद के चरणों में बहुत अधिक स्पष्ट हो जाती है। ये रुझान ग्रामीण और शहरी दोनों क्षेत्रों में समान रहते हैं। ये सभी पहलू भारत में जीवन के अनुभवों और पर्सोना को समझने के लिए प्रासंगिक हैं।

<center>
  <img src="images/nemotron_personas_india_marital_status_distribution.png" width="600px">
</center>

## Education Level by Age Group (शिक्षा और आयु वर्ग)
The heatmap below captures patterns of educational attainment across age cohorts. For example, the proportion of people classified as literate differs between younger age groups and older age groups, reflecting historical shifts in access and in social norms. The contrast in the literacy levels in the older age-groups in rural vs. urban areas is also clearly reflected in personas, with the urban population in the younger age-groups opting to pursue higher education.

नीचे दिया गया हीटमैप (heatmap) अलग-अलग आयु वर्गों में शिक्षा के स्तर के पैटर्न को दर्शाता है। उदाहरण के लिए, कम उम्र और ज़्यादा उम्र वाले आयु वर्गों के बीच साक्षर लोगों का अनुपात अलग-अलग है। यह शिक्षा तक पहुँच और सामाजिक मान्यताओं में आए ऐतिहासिक बदलावों को दर्शाता है। ज़्यादा उम्र वाले आयु वर्गों में, ग्रामीण और शहरी इलाकों के बीच साक्षरता के स्तर का यह अंतर पर्सोना में भी साफ़ तौर पर झलकता है। वहीं, युवा आयु वर्ग की शहरी आबादी उच्च शिक्षा को चुन रही है।

<center>
  <img src="images/nemotron_personas_india_education_distribution.png" width="600px">
</center>

## Geographic Intricacies of Education Attainment (शैक्षिक उपलब्धि की भौगोलिक बारीकिया)
This slice of our dataset demonstrates how geography informs education and therefore persona descriptions. The choropleth map shows, for each Indian state / union territory, the share of residents ages 25 and older who hold at least a bachelor’s degree. The generated personas also capture the contrast of rural vs. urban regions in each state / UT. No LLM in our testing was able to generate data of this fidelity.

हमारे डेटासेट का यह हिस्सा दिखाता है कि किसी जगह का भूगोल वहाँ की शिक्षा को कैसे प्रभावित करता है, और इसी से लोगों के विवरण बनते हैं। यह नक्शा दिखाता है कि भारत के हर राज्य और केंद्र-शासित प्रदेश में, 25 साल से ज़्यादा उम्र के कितने प्रतिशत निवासियों के पास कम-से-कम बैचलर डिग्री है। ये बनाए गए पर्सोना हर राज्य और केंद्र-शासित प्रदेश के ग्रामीण और शहरी इलाकों के बीच का फ़र्क भी साफ़ दिखाते हैं। हमारी टेस्टिंग में कोई भी LLM इतनी सटीक डेटा नहीं बना पाया।
<center>
  <img src="images/nemotron_personas_india_education_map.png" width="700px">
</center>

## Occupational Categories (व्यावसायिक श्रेणियाँ)
The treemap below reflects the richness of our dataset with respect to professional occupations of personas, aligned to the categories defined in the National Classification of Occupations - 2004. Represented in our dataset are over 2,900 occupation categories that are further informed by demographic and geographic distributions. This figure only shows basic occupation categories. 

नीचे दिया गया ट्रीमैप व्यक्तित्वों के व्यावसायिक व्यवसायों के संबंध में हमारे डेटासेट की समृद्धि को दर्शाता है, जो राष्ट्रीय व्यावसायिक वर्गीकरण - 2004 में परिभाषित श्रेणियों के मुताबिक है। हमारे डेटासेट में 2,900 से ज़्यादा व्यावसायिक श्रेणियां हैं जिन्हें जनसांख्यिकीय और भौगोलिक आँकड़ों द्वारा और सूचित किया जाता है। यह आंकड़ा केवल बुनियादी व्यावसायिक श्रेणियों को दिखाता है।
<center>
  <img src="images/nemotron_personas_india_occupation_tree_map.png" width="600px">
</center>

## Persona Diversity (व्यक्तित्व की विविधता)
The attributes above (and many more) ultimately affect the diversity of the synthetic personas being generated. As an example, the analysis below highlights a multitude of clusters within professional persona descriptions. These clusters are identified by clustering embeddings and reducing dimensionality to 2D. The largest cluster is representative of the non-working population which includes students, retired workers, and home-makers and the unemployed. We interpret “non-worker” in the census report as “No Occupation”. 

ऊपर दी गई विशेषताएँ (और कई अन्य) अंततः बनाए जा रहे सिंथेटिक व्यक्तित्वों की विविधता को प्रभावित करती हैं। उदाहरण के लिए, नीचे दिया गया विश्लेषण व्यावसायिक व्यक्तित्व विवरणों के भीतर कई समूहों पर प्रकाश डालता है। इन समूहों की पहचान एम्बेडिंग को क्लस्टर करके और आयामीता को 2D तक कम करके की जाती है। सबसे बड़ा क्लस्टर उस आबादी का प्रतिनिधित्व करता है, जिनके पास नौकरी नहीं है, जिसमें छात्र, सेवानिवृत्त कर्मचारी, गृहणियां और बेरोजगार लोग शामिल हैं। हम जनसांख्यिकीय रिपोर्ट में "non-worker" की व्याख्या "कोई नौकरी नहीं" के रूप में करते हैं।
<center>
  <img src="images/nemotron_personas_india_professional_personas_clustering.png" width="600px">
</center>

# How to use it (इसका उपयोग)
You can load the dataset with the following lines of code.

आप निम्नलिखित लाइनों के साथ डेटासेट लोड कर सकते हैं।

```python
from datasets import load_dataset

# English personas
nemotron_personas_en = load_dataset("nvidia/Nemotron-Personas-India", "en_IN")

# Hindi personas in Devanagari
nemotron_personas_hi_deva = load_dataset("nvidia/Nemotron-Personas-India", "hi_Deva_IN")

# Hindi personas in Latin
nemotron_personas_hi_latn = load_dataset("nvidia/Nemotron-Personas-India", "hi_Latn_IN")

```

# Dataset Characterization (डेटासेट की विशेषताएँ)

## Data Collection Method (डेटा संग्रह विधि)
* Hybrid: Human, Synthetic, Automated
* मिश्रित: मानव, सिंथेटिक, स्वचालित

## Labeling Method (लेबलिंग विधि)
* Not Applicable
* लागू नहीं

## Dataset Format (डेटासेट प्रारूप)
* Text
* टेक्स्ट

## Dataset Quantification (डेटासेट की मात्रा)
* Record counts: 3M records (21M persona descriptions)
* Total data storage: 9.6 GB

* रिकॉर्ड संख्या: 30 लाख रिकॉर्ड (2.1 करोड़ पर्सोना विवरण) 
* कुल डेटा स्टोरेज: 9.6 GB

# Ethical Considerations (नैतिक विचार):
NVIDIA believes [Trustworthy AI](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/) is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

NVIDIA का मानना है कि [विश्वसनीय AI](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/) एक साझा ज़िम्मेदारी है और हमने AI अनुप्रयोगों की एक विस्तृत श्रृंखला के विकास को सक्षम करने के लिए नीतियाँ और प्रथाएँ स्थापित की हैं। हमारी सेवा की शर्तों के अनुसार डाउनलोड या उपयोग किए जाने पर, डेवलपर्स को अपनी आंतरिक टीमों के साथ काम करके यह सुनिश्चित करना चाहिए कि यह डेटासेट संबंधित उद्योग और यूज़-केस की आवश्यकताओं को पूरा करता है और उत्पाद के अप्रत्याशित दुरुपयोग को संबोधित करता है।

कृपया सुरक्षा संबंधी कमज़ोरियों या NVIDIA AI से संबंधित चिंताओं की रिपोर्ट [यहाँ](https://www.nvidia.com/en-us/support/submit-security-vulnerability/) करें।

# Citation (उद्धरण)
If you find the data useful, please cite:

यदि आपको यह डेटा उपयोगी लगता है, तो कृपया इसे इस प्रकार उद्धृत करें:
```
@software{nvidia/Nemotron-Personas-India,
  author = {Praveen, Kiran and Vaidya, Utkarsh and Acharya, Evan and Ramaswamy, Lipika and Nathawani, Dhruv and Corneil, Dane and Meyer, Yev},
  title = {{Nemotron-Personas-India: Synthetic Personas Aligned to Real-World Distributions for India},
  month = {October},
  year = {2025},
  url = {https://huggingface.co/datasets/nvidia/Nemotron-Personas-India}
```
