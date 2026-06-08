// Lấy danh sách sinh viên từ backend và hiển thị lên table
function fetchStudents() {
    axios.get('http://localhost:5000/api/students')  // Thay thế URL với backend của bạn
        .then(response => {
            const students = response.data;
            const studentTable = document.querySelector('#studentTable tbody');
            studentTable.innerHTML = ''; // Xóa dữ liệu cũ trong bảng

            students.forEach(student => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${student.name}</td>
                    <td>${student.age}</td>
                    <td>${student.class}</td>
                    <td>
                        <button class="delete" onclick="deleteStudent(${student.id})">Xóa</button>
                    </td>
                `;
                studentTable.appendChild(row);
            });
        })
        .catch(error => console.error('Lỗi khi lấy danh sách sinh viên:', error));
}

// Thêm sinh viên mới
const addStudentForm = document.getElementById('addStudentForm');
addStudentForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Ngừng hành động mặc định (nạp lại trang)

    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const className = document.getElementById('class').value;

    const newStudent = {
        name: name,
        age: age,
        class: className
    };

    axios.post('http://localhost:5000/api/students', newStudent)  // Thay thế URL với backend của bạn
        .then(response => {
            fetchStudents(); // Lấy lại danh sách sinh viên sau khi thêm mới
        })
        .catch(error => console.error('Lỗi khi thêm sinh viên:', error));
});

// Xóa sinh viên
function deleteStudent(id) {
    axios.delete(`http://localhost:5000/api/students/${id}`)  // Thay thế URL với backend của bạn
        .then(response => {
            fetchStudents(); // Lấy lại danh sách sau khi xóa
        })
        .catch(error => console.error('Lỗi khi xóa sinh viên:', error));
}

// Khi tải trang, lấy danh sách sinh viên
window.onload = fetchStudents;
