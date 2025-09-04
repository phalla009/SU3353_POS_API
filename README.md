----Mini Inventory-----
+ Technology
 *Backend
 - Flask API
 - Postgresql
 *FrontEnd
 - Angular v20+
 - BootrapCSS
+ Project Module
 - Branch Management
 - User Management
 - Product Information Management
 - Stock Management
 - Sale Management
 - Report Management
+ Database Structure
 + branch
  - id(pk)
  - name(varchar)*
  - logo(varchar)
  - phone(varchar)
  - address(varchar)
 + user
  - id(pk)
  - branch_id(fk)*
  - username(varchar)*
  - password(varchar)*
 +  category
  - id(pk)
  - name(varchar)*
 +  product
  - id(pk)
  - name(varchar)*
  - category_id(fk)*
  - cost(decimal)*
  - price(decimal)*
  - stock(int)*
 + sale
  - id(pk)
  - date_time(datetime)*
  - user_id(fk)
  - total(decimal)*
  - paid(decimal)*
 + sale_item
  - id(pk)
  - sale_id(fk)*
  - product_id(fk)*
  - qty(int)*
  - cost(decimal)*
  - price(decimal)*