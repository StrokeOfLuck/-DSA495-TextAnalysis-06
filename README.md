# DSA 495 — Module 06: Topic Modeling Playground

A personal playground copy of Serena Kim's **DSA495 Module 06** notebook for experimenting with BERTopic, UMAP, HDBSCAN, c-TF-IDF, topic visualizations, and outlier analysis.

## Open in Google Colab

[Open DSA495-M06-Topic-Modeling.ipynb in Colab](https://colab.research.google.com/github/StrokeOfLuck/-DSA495-TextAnalysis-06/blob/main/DSA495-M06-Topic-Modeling.ipynb)

## Files

- `DSA495-M06-Topic-Modeling.ipynb` — original Module 06 class notebook
- `data/README.md` — where to put the prepared CSV

## Data needed

The notebook expects:

```
news_category_2022.csv
```

The original class notebook points to a course-specific Google Drive path:

```python
/content/drive/MyDrive/a-ncsu-courses/DSA495-2026/Data/M06_TopicModeling/news_category_2022.csv
```

For this playground, the cleanest option is to put the CSV at:

```
data/news_category_2022.csv
```

and change the notebook's `DATA_PATH` line to:

```python
DATA_PATH = Path("/content/-DSA495-TextAnalysis-06/data/news_category_2022.csv")
```

when running after cloning the repo in Colab.

## Original source

Class material:
https://github.com/SerenaYKim/DSA495-TextAnalysis/tree/master/Module06

This repo is for experimentation so you can change parameters, labels, visualizations, and clustering settings without touching the class repository.
