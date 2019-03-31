---
title: Automated testing
teaching: 0
exercises: 0
questions:
- "Why does testing need to be part of the software development cycle?"
- "how can software development cycle be implemented?"
objectives:
- "Learn about automated testing with pytest"
- "Learn about travis and how to use it"
keypoints:
- "collaborative testing/code review workflow"
- "pytest"
- "travis"
---

We use [CodeRefinery](https://coderefinery.org/) lesson on [Automated testing](https://coderefinery.github.io/testing/).



# Automated testing

In this lesson we will discuss why testing needs to be part of the software
development cycle and how such a cycle can be implemented. We will exercise a
collaborative testing/code review workflow.


## Prerequisites

1. You need [pytest](http://doc.pytest.org) (as part of Anaconda or Miniconda or Virtualenv).

2. Basic understanding of Git.

3. You need a [GitHub](https://github.com) account.

4. You will also need a [Travis CI](https://travis-ci.org) account
   but you can sign into it with
      your [GitHub](https://github.com) account.


# Automated testing in practice

- [Motivation](https://coderefinery.github.io/testing/01-motivation/)
- [Concepts](https://coderefinery.github.io/testing/02-concepts/)
- [Tools](https://coderefinery.github.io/testing/03-frameworks/)
- [Exercise: testing with pytest](https://coderefinery.github.io/testing/04-pytest/)
- [Exercise/discussion: Testing using hooks](https://coderefinery.github.io/testing/05-pre-commit-hook/)
- [Exercise: Automatic testing with Travis CI](Exercise: Automatic testing with Travis CI)
- [Exercise/discussion: Test design](https://coderefinery.github.io/testing/08-test-design/)

# Conclusions and recommendations


- Explore and use the good tools that exist out there
- Automatize
- Strike a healthy balance between unit tests and integration tests
- Require that new functionality comes with new tests
- When you discover and fix a bug, also commit a test against this bug
- Use code coverage analysis to identify untested code or dead wood


{% include links.md %}
