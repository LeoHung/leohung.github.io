---
layout: page
title: "San-Chuan (Leo) Hung"
date: 2014-08-31 22:27
comments: false
sharing: false
footer: false
save_as: index.html
---

  I'm San-Chuan "Leo" Hung(洪三權), studying in Carnegie Mellon University, specifying in Computation Data Science (a.k.a MCDS and VLIS), grduating in December 2015.

  contact: c2016.tw at gmail.com

<a id="education"></a>
# Education

  ![cmu](/images/education/cmu.jpg){: style="float:right; width:80px; height:80px"}

#### Carnegie Mellon University, Pittsburgh, PA (December 2015)
  * School of Computer Science, Master of Computational Data Science
  * GPA: 3.9/ 4.0
<div class="clearfix"></div>

  ![ntu](/images/education/ntu.jpg){: style="float:right; width:80px; height:80px"}

#### National Taiwan University, Taipei, Taiwan (January 2013)
  * Department of Computer Science and Information Engineering, M.S. in Computer Science
  * GPA: 4.1/ 4.0

  ![ntu](/images/education/ntu.jpg){: style="float:right; width:80px; height:80px"}

#### National Taiwan University, Taipei, Taiwan (January 2011)
  * Department of Computer Science and Information Engineering, B.S. in Computer Science (Double Major in Sociology)
  * GPA: 3.9/ 4.0

<a id="experience"></a>
# Experience

  ![whoscall](/images/experience/whoscall.png){: style="float:right; width:80px; height:80px"}

#### Intern, Gogolook Co., Ltd, Taipei, Taiwan (March - July 2014)

  Designed and programmed the first version of a realtime back-end API server with an analytic dashboard for a mobile app with more than 10 million global users

  Technologies: Python, MongoDB, BigQuery, Git, CSS, HTML

  ![whoscall](/images/experience/taichung.gif){: style="float:right; width:80px; height:80px"}

#### Substitute Military Service (Social Service), Social Affairs Bureau of Taichung City Government (February 2013 - February 2014)

  Assisted IT managers in maintaining existing systems and developed novel information systems, for which I received the prize for honored Substitute Military Servicemen

  Technologies: PHP, codeigniter, jQuery, CSS

  ![whoscall](/images/experience/yahoo.jpg){: style="float:right; width:80px; height:80px"}

#### Intern, Search Team, Yahoo! Taiwan (August - September 2011)

  Analyzed mobile search engine query log and implemented a location-based query suggestion system which can improve speed for user typing query by 180%.

  Technologies: Natural Language Processing, Python, C, Pig, Hadoop

<a id="projects"></a>
# Academic Projects

#### "EazyMP," Parallel Computer Architecture and Programming, CMU (May 2015)

  A python translator which help users easily and lazily convert their sequential python code to process-parallel python code

- Use OpenMP style annotation ("#pragma omp parallel for") to make for-loop running in parallel
- Experiments on multi-cores cluster shows that EazyMP can provide scalable speedup( N/2x ~ Nx )
- It is open source now. [link](http://leohung.net/eazymp)

  Technologies: Parallel Programming, Python

#### "Memmetric," Big Data Studio, CMU (May 2015)

  A Hadoop memory usage monitor specifies based on Ganglia and Hadoop 1.2.1

  - Fix a bug in Hadoop class (GanagliaSink31.java)
  - Implement a frontend to present real-time memory usage and historical memory usage
  - Analyze three types of memory failure: JVM Heap Size Error, TaskMemoryManagerThread, and Execessive Slots.

  <center>
  ![Memmetric](/images/memmetric/overview.png){: style=" width:500px"}
  </center>

  Technologies: Hadoop 1.x, Ganglia, Javascript, HTML, CSS

#### "Tweet Analysis System Competition," Cloud Computing, CMU (Dec 2014)

  Applied ETL on 1TB twitter data to build a high performance web-based query system under very limited budget, ranked 13th over 91 teams

- Developed a high performance(rps > 5000~15000) web API server for 6 types of query with Undertow framework
- Tuned HBase and MySQL clusters to reduce response time
- Utilized multiple caching strategy to improve throughput

  Technologies: API Server, AWS EC2, HBase, MySQL, Hadoop, JAVA

#### "MapReduce Engine," Distributed System, CMU (Dec 2014)

  Built a simplified MapReduce framework from scratch: including a MapReduce computing framework and a distributed file system

- Designed and implemented job trackers, task trackers, schedulers to dispatch and execute map tasks and reduce tasks
- Designed and implemented fault-tolerance mechanism for the MapReduce framework

  Technologies: Distributed System, MapReduce, JAVA, RMI

#### "GraphMiner," Multimedia Databases and Data Mining, CMU (Dec 2014)

  Enhanced a SQL-based graph mining tool and mined 20 network data

- Implemented K-Core detection algorithm in GraphMiner
- Improved GraphMiner speed with SQL index caching
- Mined degree distribution, triangle counting, giant connected component, Page Rank, K-Core on 20 network data

  Technologies: Data Mining, Social Network Analysis, PostgreSQL, Python

#### "Multiclass Image Object Classification," Machine Learning, CMU (Dec 2014)

   Classified images into 10 labels with Neural Network, Random Forest, Multinomial Logistic Regression, and Supported Vector Machine

- Extracted image features, like color histogram and edge, from original images
- Developed an ensemble method, which can improved performance by 0.76% ~ 13.07%

  Technologies: Machine Learning, Matlab, Weka

# Personal Projects

#### <a href="http://leohung.net/taiwancolors/about/">"Taiwan Colors"</a>

   Taiwan colors palettes, automatically generated by unsupervised clustering algorithms from Taiwan pictures, to inspire next awesome design of Taiwan

   Technologies: Machine Learning, Multimedia Analysis, jQuery, CSS

   <center>
   ![Taiwan Color](/images/portofolio/taiwan_color.png)
   </center>

* * *

#### “Oh! My Type”

  A vision-based friend recommendation system

  Technologies: Multimedia Analysis, Information Retrieval, Python, C, Questionnaire study

<div class="videoWrapper">
<iframe width="560" height="349" src="//www.youtube.com/embed/56dLqu7pcqQ" frameborder="0" align="middle" allowfullscreen></iframe>
</div>
<a id="skills"></a>
# Technical Skills
- Proficient With: Python, Java, Hadoop, AWS, Distributed System, Web Development, Machine Learning, Data Mining
- Familiar With: MongoDB, HBase, MySQL, Git, HTML, CSS

<a id="publication"></a>
# Publication

#### Tsung-Ting Kuo, <b>San-Chuan Hung</b>, Wei-Shih Lin, Nanyun Peng, Shou-De Lin, and Wei-Fen Lin,
  “Exploiting latent information to predict diffusions of novel topics on social networks,” in ACL ‘12  [download](/publication/acl12.pdf)

  Predict novel topic information diffusion on social network, and the result shows 16% AUC improvement over the baseline models.

  Technologies: Social Network Analysis, Natural Language Processing, Machine Learning, JAVA, Python, C




