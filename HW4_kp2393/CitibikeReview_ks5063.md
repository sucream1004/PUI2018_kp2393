# Review of CitiBike data by Karan (ks5063)

* Null and Alternate Hypothesis
    * Null and Alternate hypothesis have been formulated correctly.

* Data processing
    * Available data does support hypothesis testing.
    * Data processing has been done to extract age.
    * Two subsets have been created based on age to separate young and old people.
    
* Comments and Suggestions
    * Interesting hypothesis and efficient data processing to support hypothesis testing.
    * Might be interesting to consider usertype as a control variable.
    * Data processing might be expanded to add a categorical variable indicating cold or hot weather to further support hypothesis testing.

* Statistical Test
    * I think ANCOVA is the most appropriate test to use here.
    * ANCOVA answers the question ("Do differences exist between 2 or more groups after controlling for CVs on one DV?").[https://github.com/fedhere/UInotebooks/blob/master/slides2018/UI5_PUI2018.pdf]
    * In this hypothesis it translates to : Do differences exist between young and elder people after controlling for usertype on percent of ridership during winter in comparison to summer?