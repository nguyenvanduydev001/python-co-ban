import pandas as pd

du_lieu = {
    'Name': ['A', 'Binh', 'Chi', 'Dung', 'Hai', 'Uy', 'Linh', 'Việt', 'Son', 'Duy'],
    'Age': [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
    'Gender': ['M', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F'],
    'Score': [8.5, 6.0, 4.5, 7.0, 9.0, 5.5, 3.0, 10.0, 2.5, 6.5]
}

df_students = pd.DataFrame(du_lieu, index=range(1, 11))

print("Toàn bộ danh sách sinh viên:")
print(df_students)

print("\n3 dòng đầu tiên:")
print(df_students.head(3))

print("\nTên sinh viên ở dòng số 2:")
print(df_students.loc[2, 'Name'])

print("\nTuổi của sinh viên ở dòng số 10:")
print(df_students.loc[10, 'Age'])

print("\nChỉ hiện cột Tên và Điểm:")
print(df_students[['Name', 'Score']])

df_students['Pass'] = df_students['Score'] >= 5

print("\nBảng sau khi thêm cột 'Pass':")
print(df_students)

df_sorted = df_students.sort_values(by='Score', ascending=False)

print("\nDanh sách sinh viên theo điểm giảm dần:")
print(df_sorted)
