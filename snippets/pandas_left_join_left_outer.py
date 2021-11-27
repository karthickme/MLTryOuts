import pandas as pd

left = pd.DataFrame({
    'Sr': [6, 7, 8, 9, 2],
    'Name': ['Span', 'Suchu', 'Vetts', 'Appu', 'Sri']})
right = pd.DataFrame({
    'Sr': [6, 7, 8, 9, 4],
    'Name': ['fil', 'mil', 'sil', 'pil', 'gil']})
print(pd.merge(left, right, on='Sr', how='left'))

print(pd.merge(left, right, on='Sr', how='outer'))
