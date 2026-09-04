---
layout: minimal
title: EECS 245 Exams
nav_order: 1
---

<style>
#main-header,
.site-header,
.aux-nav,
.main-header {
  display: none !important;
}

body {
  padding-top: 0 !important;
}

.main-content-wrap {
  margin-top: 0 !important;
}
</style>

# EECS 245 Exams

A repository of past exams and solutions for EECS 245: Mathematics for Machine Learning at the University of Michigan. See the course website [here](https://eecs245.org).

{: .yellow }
> If there are formatting issues or ambiguities with any of the questions, please let Suraj know at rampure@umich.edu!

## Past Exams

All exams in EECS 245 are designed to be completed in 2 hours.

{% comment %}
One row per term, one cell per exam, straight from _data/exams.yml -- adding an
exam there adds it here. The leading separator makes a header-less table. No
whitespace-trimming tags here: the blank line above the table is what makes
kramdown start a table instead of continuing the paragraph.
{% endcomment %}
{% assign terms = site.data.exams | group_by: "term" %}
| --- | --- | --- | --- |
{% for term in terms -%}
| {{ term.name }} |{% for exam in term.items %} [{{ exam.label | default: exam.exam }}](exams/{{ exam.id }}/) |{% endfor %}
{% endfor %}

## Problems by Topic

Worksheets of past exam problems organized by chapter of the [course notes](https://notes.eecs245.org), with solutions included as dropdowns.

1. [Introduction to Supervised Learning](/worksheets/chapter-1/)
2. [Simple Linear Regression](/worksheets/chapter-2/)
3. [Vectors](/worksheets/chapter-3/)
4. [Linear Independence](/worksheets/chapter-4/)
5. [Matrices](/worksheets/chapter-5/)
6. [Linear Transformations and Projections](/worksheets/chapter-6/)
7. [Regression Using Linear Algebra](/worksheets/chapter-7/)
8. [Gradients](/worksheets/chapter-8/)
9. [Eigenvalues and Eigenvectors](/worksheets/chapter-9/)
10. [Singular Value Decomposition](/worksheets/chapter-10/)

---

<small>Thanks to former student Jack Taylor for working on this site!</small>