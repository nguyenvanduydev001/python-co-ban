# Bắt đầu bằng cách nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo dữ liệu danh sách sinh viên dưới dạng từ điển (dictionary)
du_lieu = {
    'Name': ['A', 'Binh', 'Uy', 'Dung', 'Hai', 'Hung', 'Duy', 'Mai', 'Son', 'Việt'],
    'Age': [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
    'Gender': ['M', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F'],
    'Score': [8.5, 6.0, 4.5, 7.0, 4.0, 5.5, 3.0, 10.0, 8.5, 6.5]
}

# Tạo bảng dữ liệu (DataFrame) từ dữ liệu trên
# Index sẽ bắt đầu từ 1 cho giống số thứ tự sinh viên
df_students = pd.DataFrame(du_lieu, index=range(1, 11))

# Hiển thị toàn bộ dữ liệu
print("Toàn bộ danh sách sinh viên:")
print(df_students)

# Hiển thị 3 dòng đầu tiên của bảng
print("\n3 dòng đầu tiên:")
print(df_students.head(3))

# Lấy tên của sinh viên có index = 2
print("\nTên sinh viên ở dòng số 2:")
print(df_students.loc[2, 'Name'])

# Lấy tuổi của sinh viên ở dòng số 10
print("\nTuổi của sinh viên ở dòng số 10:")
print(df_students.loc[10, 'Age'])

# Hiển thị 2 cột: Name và Score
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
