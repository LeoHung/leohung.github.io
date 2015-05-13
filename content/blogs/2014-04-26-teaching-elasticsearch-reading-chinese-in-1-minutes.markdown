---
layout: post
title: "Teaching Elasticsearch reading Chinese in 1 Minutes "
date: 2014-04-26 19:07
comments: true
categories: Elasticsearch, Chinese, Analyzer
---
# Teaching Elasticsearch reading Chinese in 1 Minutes


Elasticsearch(es) is a powerful open source solution for searching, which is serving in wikipedia currently; however, Chinese users is not so lucky with es, becasue the default analyzer of es cannot deal with Chinese well, which will tokenzie Chinese sentences into individual characters, rather than terms, causing large amount of noise in retrieved results.

To enhance the performance of retrieval, setting the analyzer is necessary; however, there is no quick and effective plug-in for traditional Chinese. IKAnalyzer, developed by China community, may be the best plug-in for Chinese Elasticsearch engineers to serve the job, but IKAnalyzer cannot be set easily.

If you just want a quick solution, cjk analyzer is the best solution. The algorithm of cjk analyzer is easy to be understood: tokenizing sentences to  bi-gram terms. For example, "我愛吃飯" will be transformed into "我愛", "愛吃", "吃飯". The analyzer is naive but powerful to enhance es performance.

The below is the setting syntax :

    PUT "index name"
    "settings": {
         "analysis":{
            "analyzer":{
                "default":{"type":"cjk"}
            }
         }
    }

Beware, the setting only work when the index is empty. If there are data in the index, do not forget to re-index it.

#一分鐘搞定Elasticsearch中文設定

Elasticsearch(es)是一套強大的搜尋引擎套件，目前維基百科正是使用es作為搜尋套件。但是，es的預設設定對中文使用者並不是很友善，因為es預設的分析器(Analyzer)不能處理好中文的斷詞(tokenization)，會把中文詞切成一個字一個字，而非以詞組為單位，使得搜尋效果變差，時常會搜尋到過多雜訊。

因此，需要設定好es的斷詞設定，才能強化中文搜尋的結果。但可惜的是，繁體中文並沒有已經被最佳化的套件可以無痛與es接軌。目前已知比較好的方案，像是中國社群(誰?)發展出 IKanalyzer ，但需要花一點時間做複雜的設定。

如果只是短期內需要一個堪用的做法，可以試試看cjk分析器。cjk分析器的原理很簡單，也就只是做 Bi-Gram，把讀進來的句子，兩個兩個切成一個詞。例如：「我愛吃飯」，就變成「我愛, 愛吃, 吃飯」。簡單的設定，就可以強化es的搜尋結果。

設定的語法如下：

    PUT "index name"
    "settings": {
         "analysis":{
            "analyzer":{
                "default":{"type":"cjk"}
            }
         }
    }

請注意，settings必須在index剛建立之初設定才有效。如果index裡面已經有資料，請reindex你的資料庫。
