# Flask Mini Project

## 1. What and Why Flask-Extension?
**Flask-Extension** គឺជាបណ្ណាល័យបន្ថែម (plugin) ដែលជួយពង្រីកសមត្ថភាពរបស់ Flask។  
- **ហេតុអ្វីត្រូវប្រើ?**
  - បន្ថែមមុខងារដែល Flask ដើមគ្មាន (ex: Database, Form Validation, Authentication)។
  - ជួយឲ្យការអភិវឌ្ឍមានប្រសិទ្ធភាព និងកាត់បន្ថយកូដដែលត្រូវសរសេរដោយខ្លួនឯង។
  - ឧទាហរណ៍៖ `Flask-SQLAlchemy`, `Flask-Migrate`, `Flask-Login`។

---

## 2. What and Why Flask-Migration?
**Flask-Migrate** គឺជាឧបករណ៍ Migration សម្រាប់ Database ដែលផ្អែកលើ Alembic។  
- **ហេតុអ្វីត្រូវប្រើ?**
  - អាច Update Database Structure ដោយមិនបាត់ទិន្នន័យចាស់។
  - គ្រប់គ្រង Version Database (Rollback/Upgrade) បានងាយស្រួល។
  - ឧទាហរណ៍៖ បន្ថែម Column ថ្មីទៅក្នុង Table ដោយមិនចាំបាច់ Drop Database ចាស់។

---

## 3. Database Structure

### branch
- `id` (pk)  
- `name` (varchar)*  
- `phone` (varchar)*  
- `address` (varchar)  
- `description` (varchar)  

### customer
- `id` (pk)  
- `username`  
- `email` (varchar)*  
- `password` (varchar)*  
- `remark` (varchar)  

### user
- `id` (pk)  
- `username`  
- `email` (varchar)*  
- `password` (varchar)*  
- `remark` (varchar)  

### category
- `id` (pk)  
- `name` (varchar)*  

### product
- `id` (pk)  
- `name` (varchar)*  
- `category_id` (fk)*  
- `cost` (decimal)*  
- `price` (decimal)*  
- `image` (varchar)  
- `stock` (decimal)* - default: 0  
- `description` (varchar)  

### customer_cart
- `id` (pk)  
- `customer_id` (fk)*  
- `product_id` (fk)*  
- `qty` (int)*  

### order
- `id` (pk)  
- `user_id` (fk)*  
- `customer_id` (fk)*  
- `date_time` (datetime)*  
- `status` (pending, …)  

### order_item
- `id` (pk)  
- `order_id` (fk)*  
- `product_id` (fk)*  
- `price` (int)*  
- `qty` (int)*  
- `total` (decimal)*  

---


