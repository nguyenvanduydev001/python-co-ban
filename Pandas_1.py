import pandas as pd

# Tạo dữ liệu danh sách sinh viên 
du_lieu = {
    'Name': ['A', 'Binh', 'Phong', 'Dung', 'Hai', 'Uy', 'Linh', 'Mai', 'Son', 'Duy'],
    'Age': [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
    'Gender': ['M', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F'],
    'Score': [8.5, 6.0, 4.5, 7.0, 4.0, 5.5, 3.0, 10.0, 8.5, 6.5]
}

# Tạo bảng dữ liệu (DataFrame)
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

# Thêm cột mới tên là 'Pass'
# Nếu Score >= 5 thì Pass là True (qua môn), ngược lại là False (trượt)
df_students['Pass'] = df_students['Score'] >= 5

# Hiển thị lại bảng sau khi thêm cột Pass
print("\nBảng sau khi thêm cột 'Pass':")
print(df_students)

# Sắp xếp sinh viên theo điểm từ cao xuống thấp
df_sorted = df_students.sort_values(by='Score', ascending=False)

print("\nDanh sách sinh viên theo điểm giảm dần:")
print(df_sorted)
