---
permalink: /
title: ""
excerpt: ""
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<header class="lab-home-heading">
  <h1>Yin Research Lab at the University of South Carolina</h1>
  <a class="lab-home-heading__logo-link" href="https://sc.edu/study/colleges_schools/engineering_and_computing/" aria-label="Visit the Molinaroli College of Engineering and Computing website">
    <img src="{{ '/images/USC_Molinaroli_logo_centered_RGB_2C.png' | relative_url }}" alt="University of South Carolina Molinaroli College of Engineering and Computing">
  </a>
</header>

<section class="lab-section">
  <div class="lab-section__heading">
    <p class="lab-eyebrow lab-eyebrow--editorial">Our mission</p>
    <h2>Decision intelligence that works beyond the benchmark</h2>
  </div>
  <div class="lab-section__copy">
    <p>The research lab is goal-driven and aims to advance decision intelligence and sustainable computing for complex systems.</p>
    <p>Our research brings together operations research and responsible AI/ML. We study how intelligent decision systems can generalize to new conditions, operate under finite computational budgets, and deliver net sustainability benefits when deployed at scale.</p>
  </div>
</section>

<div class="lab-card-grid lab-card-grid--three">
  <article class="lab-card">
    <span class="lab-card__number">01</span>
    <h3>AI + Optimization</h3>
    <p>Learning-augmented and generative-AI methods for combinatorial optimization and sequential decision-making.</p>
  </article>
  <article class="lab-card">
    <span class="lab-card__number">02</span>
    <h3>Mobility + Logistics</h3>
    <p>Data-driven planning and operations for shared mobility, urban transportation, e-commerce, and supply chains.</p>
  </article>
  <article class="lab-card">
    <span class="lab-card__number">03</span>
    <h3>Sustainable AI systems</h3>
    <p>Life-cycle evaluation and system design that account for the environmental costs and benefits of AI.</p>
  </article>
</div>

<figure class="lab-summary-figure">
  <img src="{{ '/images/research_teaching_summary.png' | relative_url }}" alt="Overview of the lab's research methodology, application areas, responsible AI work, and teaching philosophy">
</figure>

<section class="lab-pi">
  <img src="{{ '/images/headshot_Zhuoli_2025.jpg' | relative_url }}" alt="Zhuoli Yin" class="lab-pi__photo">
  <div>
    <p class="lab-eyebrow">PRINCIPAL INVESTIGATOR</p>
    <h2>Zhuoli Yin</h2>
    <p class="lab-pi__affiliation"><strong>Assistant Professor</strong><br>Industrial Engineering Program, Department of Mechanical Engineering<br>University of South Carolina</p>
    <p>Zhuoli Yin develops AI-augmented optimization systems for transportation, logistics, and sustainable computing. His work spans the full research lifecycle—from problem formulation and algorithm design to large-scale simulation and deployment.</p>
    <p>He earned his Ph.D. and M.S. in Industrial Engineering from Purdue University and his B.E. in Electronic and Information Engineering from Beihang University.</p>
    <p><a href="{{ '/pdf/Zhuoli_Yin_Academic_CV.pdf' | relative_url }}">Curriculum vitae</a> · <a href="https://scholar.google.com/citations?user=Zu69_1AAAAAJ">Google Scholar</a></p>
    <p><strong>Office:</strong> {{ site.author.office }} · <strong>Address:</strong> {{ site.author.address }}<br><strong>Email:</strong> {{ site.author.email_display }}</p>
  </div>
</section>

<p class="lab-recruitment-notice">Yin Lab is looking for highly motivated PhD students starting from Spring or Fall 2027. Please check <a href="{{ '/prospective-students/' | relative_url }}">Prospective Students</a>.</p>

<aside class="lab-callout">
  <div>
    <p class="lab-eyebrow">JOIN US</p>
    <h2>Curious minds are welcome.</h2>
    <p>We welcome prospective Ph.D., master's, and undergraduate students who want to work at the intersection of AI, optimization, and real-world systems.</p>
  </div>
  <a class="lab-button lab-button--light" href="{{ '/prospective-students/' | relative_url }}">For prospective students</a>
</aside>


# 🔥 News
- **08/2026:** I joined the University of South Carolina as an Assistant Professor and am recruiting Ph.D. students to join my research lab.
- 07/2026: I successfully defended my Ph.D. thesis titled "Learning-Augmented Optimization Systems”. I really appreciate my advisor, Dr. Hua Cai, and my advisory committee! 🎓
- 05/2026: I will attend the 2026 IISE Annual Conference in Arlington, TX, where I will present my latest work on the sustainable use of AI for optimization. I will also join as a panelist for "Does AI Belong at the Sustainability Table? A Live Multi-AI Panel on Technology, Conscience, and Climate." Please feel free to come say hi!
<!-- - 05/2026: I will join the [Department of Mechanical Engineering](https://sc.edu/study/colleges_schools/engineering_and_computing/departments/mechanical_engineering/) (Industrial Engineering Program) at the University of South Carolina as a Tenure-track Assistant Professor in Fall 2026. I am recruiting highly motivated PhD students to join my lab, with fully funded positions available. Please feel free to reach out. -->
- 03/2026: I received the [Estus H. and Vashti L. Magoon Research Excellence Award](https://engineering.purdue.edu/Engr/People/Awards/Graduate/ptRecipientListing?group_id=237384&show_sub_groups=1) from the College of Engineering (COE) at Purdue University. I am grateful to my advisor, Dr. Hua Cai, and to the COE for their support.
- 01/2026: Our paper on [VLM-guided optimization for solving large-scale TSP](https://arxiv.org/abs/2509.23465) is accepted to [ICLR 2026](https://iclr.cc/)! Thanks to all the authors!
- 01/2026: Our paper ["Arthur: An Artificial Intelligence Powered Teaching Assistant System for Engineering Economics Class"](https://doi.org/10.1016/j.ijaied.2026.100003) has just been accepted by [*International Journal of Artificial Intelligence in Education*](https://www.sciencedirect.com/journal/international-journal-of-artificial-intelligence-in-education) and it is now published online. ~~Stay tuned for the online version!~~
- 08/2025: Our paper ["Enhanced global oil spill dataset from 1967 to 2023 based on text-form incident information"](https://www.nature.com/articles/s41597-025-05601-9) has been published online in *Scientific Data*.
- 06/2025: I joined Amazon as an applied scientist intern in NYC🗽.
- 05/2025: I will attend IISE annual conference 2025 and present three works.
- 04/2025: I received a Graduate Research Grant from Purdue’s Institute for a Sustainable Future (ISF) to support my research on assessing AI models' carbon footprint.
- 04/2025: I have passed my Ph.D. prelim exam. Many thanks to my advisor and committee members for their continued support!
- 10/2024: I am honored to have been selected as a 2024–2025 IISE Future Faculty Fellow. I am fortunate to be paired with [Prof. Uday Venkatadri](https://www.dal.ca/faculty/engineering/industrial/faculty-staff/our-faculty1/professors/uday-venkatadri.html) as my mentor! 
- 08/2024: I attend [NSF Workshop on Sustainable Computng](https://nsf-desc-2024.github.io/) held at Purdue on Aug 20-21
- 10/2023: I received 2023-2024 Lee A. Chaden Fellowship in Industrial Engineering at Purdue.
- 09/2023: *Purdue Today* featured our story on [Arthur](https://www.purdue.edu/studentsuccess/news/09_07_23.html), an AI-powered teaching assistant tool designed to support engineering education.
- 08/2023: I will be lecturing IE343 Engineering Economics with ~150 undergraduate students. Looking forward to the new semester!
  
# 💻 Internships
- *06/2025 - 09/2025*, **Amazon.com, Applied Scientist Intern, New York, NY.**
  - Global Transportation Services, hosted by [Dr. Golnush Amoli](https://www.linkedin.com/in/golnush-masghati-amoli-30606592/) & [Hana Ku](https://www.linkedin.com/in/kuhana/)
  - Developed Amazon's next-generation AI-driven tools to advance resilient and dynamic transportation network design.
  - Led the full lifecycle from conceptualization, multi-source data analysis, large-scale simulation, AI model training, and minimum viable product delivery.

# 📝 Publications 
- <span class="badge badge-preprint">Just Accepted 2026</span>
  ViTSP: A Vision Language Models Guided Framework for Large-Scale Traveling Salesman Problems<br>
  **Zhuoli Yin**, Yi Ding, Reem Khir, & Hua Cai  [📄 Paper](https://arxiv.org/pdf/2509.23465) \
  ICLR'26: The 14th International Conference on Learning Representations
- <span class="badge badge-preprint">Just Accepted 2026</span>
  Arthur: An Artificial Intelligence Powered Teaching Assistant System for Engineering Economics Class <br>
  **Zhuoli Yin**, Erhan Karakaya, Kalei Bass, & Hua Cai \
  International Journal of Artificial Intelligence in Education. 2026.
- <span class="badge badge-preprint">Preprint 2025</span>
  DeepBike: A Deep Reinforcement Learning Based Model for Large-scale Online Bike Share Rebalancing <br>
  **Zhuoli Yin**, Zhaoyu Kou, & Hua Cai  [📄 Paper](https://assets-eu.researchsquare.com/files/rs-3998473/v1_covered_2f3e5b57-935c-4d98-9d01-907b9a688ef0.pdf)
- Enhanced global oil spill dataset from 1967 to 2023 based on text-form incident information<br>
  Yiming Liu, **Zhuoli Yin**, & Hua Cai \
  Scientific Data, 12(1), 1-14. 2025. [📄 Paper](https://www.nature.com/articles/s41597-025-05601-9)
- Understanding the Demand Predictability of Bike Share Systems: A Station-Level Analysis<br>
  **Zhuoli Yin**, Kendrick Hardaway, Yu Feng, Zhaoyu Kou, & Hua Cai \
  Frontiers of Engineering Management, 1-15. 2023. [📄 Paper](https://link.springer.com/article/10.1007/s42524-023-0279-8)
-  A Deep Reinforcement Learning Model for Large-Scale Dynamic Bike Share Rebalancing with Spatial-Temporal Context<br>
  **Zhuoli Yin**, Zhaoyu Kou, & Hua Cai \
  The 12th International Workshop on Urban Computing. 2023. [📄 Paper](http://urban-computing.com/urbcomp2023/file/UrbComp2023_paper_7.pdf)

# 🎖 Selected Awards
- *05/2025* IISE Doctoral Colloquium (3 participants nominated per department)
- *05/2025* NSF IISE Annual Conference Student Travel Award
- *10/2024* 2024-2025 IISE Future Faculty Fellow (15 participants selected per year)
- *10/2023* 2023-2024 Lee A. Chaden Fellowship in Industrial Engineering, Purdue University
- *05/2023* Graduate School Summer Research Grant, Purdue University
- *09/2022* Honorable Mention Poster Award, Purdue Engineering Graduate Showcase

# 📚 Teaching
- **Graduate Lecturer**, *Purdue IE 343: Engineering Economics*, Fall 2023 (150 students)
- **Guest Lecturer**, *Purdue EEE 560: Environmental Data Science*, Fall 2024
- **Teaching Assistant**, *Purdue IE 343: Engineering Economics*, Fall 2021 - Fall 2025 (10 sessions in total)
- **Teaching Assistant**, *Purdue IE 590/EEE 595: Urban Mobility Optimization*, Spring 2024

# 🔍 Mentorship
**Undergraduate Students**
- Laura Almeida Tinjaca (National University of Colombia-Purdue Program)
- Quan The Dinh (Purdue, Computer Science)
- Karen Fortunat (Purdue, Industrial Engineering)
- Kalei Bass (Purdue, Industrial Engineering)

# 💪 Services
**Selected Internal Service at Purdue**
- *10/2023 - 12/2023*: Student representative on the faculty search committee
- *05/2022 - 05/2023*: Vice President, Industrial Engineering Graduate Student Organization (IEGSO)

 **Selected External Service to Professional Societies**
- *09/2023*: Support team, 2023 Purdue Research Symposium on Operations
- *05/2022*: Session chair, IISE Annual Conference & Expo 2022

**Conference Reviewer** 
- Transportation Research Board Annual Meeting (TRB) 2026
- Neural Information Processing Systems (NeurIPS) 2025
- International Symposium for Sustainable Systems and Technology (ISSST) 2024

**Journal Reviewer**
- Journal of Cleaner Production
- Networks and Spatial Economics

<!--
# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)
-->
