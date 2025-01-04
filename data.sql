-- Inserting 10 departments --
INSERT INTO directory_department (name)
VALUES

    ('Software Development'),
    ('Quality Assurance'),
    ('Human Resources'),
    ('Project Management'),
    ('DevOps'),
    ('User Experience (UX) Design'),
    ('Product Management'),
    ('IT Support'),
    ('Sales and Marketing'),
    ('Customer Success');

-- Inserting 100 employees with random departments --
INSERT INTO directory_employee (first_name, last_name, gender, address, phone_number, email, department_id, salary)
VALUES

('John', 'Doe', 'M', '123 Maple St.', '5551000001', 'john.doe@usaexample.com', 1, 5500),
('Jane', 'Smith', 'F', '456 Oak St.', '5551000002', 'jane.smith@usaexample.com', 2, 6500),
('Michael', 'Johnson', 'M', '789 Pine St.', '5551000003', 'michael.johnson@usaexample.com', 3, 7500),
('Emily', 'Williams', 'F', '101 Birch St.', '5551000004', 'emily.williams@usaexample.com', 4, 8500),
('David', 'Brown', 'M', '202 Cedar St.', '5551000005', 'david.brown@usaexample.com', 5, 9500),
('Linda', 'Davis', 'F', '303 Cherry St.', '5551000006', 'linda.davis@usaexample.com', 6, 10500),
('James', 'Martinez', 'M', '404 Ash St.', '5551000007', 'james.martinez@usaexample.com', 7, 11500),
('Laura', 'Miller', 'F', '505 Elm St.', '5551000008', 'laura.miller@usaexample.com', 8, 12500),
('Robert', 'Wilson', 'M', '606 Maple St.', '5551000009', 'robert.wilson@usaexample.com', 9, 13500),
('Olivia', 'Moore', 'F', '707 Oak St.', '5551000010', 'olivia.moore@usaexample.com', 10, 14500),
('William', 'Taylor', 'M', '808 Pine St.', '5551000011', 'william.taylor@usaexample.com', 1, 5500),
('Sophia', 'Anderson', 'F', '909 Birch St.', '5551000012', 'sophia.anderson@usaexample.com', 2, 6500),
('Benjamin', 'Thomas', 'M', '1000 Cedar St.', '5551000013', 'benjamin.thomas@usaexample.com', 3, 7500),
('Chloe', 'Jackson', 'F', '1111 Cherry St.', '5551000014', 'chloe.jackson@usaexample.com', 4, 8500),
('Ethan', 'White', 'M', '1212 Ash St.', '5551000015', 'ethan.white@usaexample.com', 5, 9500),
('Isabella', 'Harris', 'F', '1313 Elm St.', '5551000016', 'isabella.harris@usaexample.com', 6, 10500),
('Mason', 'Clark', 'M', '1414 Maple St.', '5551000017', 'mason.clark@usaexample.com', 7, 11500),
('Harper', 'Lewis', 'F', '1515 Oak St.', '5551000018', 'harper.lewis@usaexample.com', 8, 12500),
('Alexander', 'Walker', 'M', '1616 Pine St.', '5551000019', 'alexander.walker@usaexample.com', 9, 13500),
('Avery', 'Young', 'F', '1717 Birch St.', '5551000020', 'avery.young@usaexample.com', 10, 14500),
('Jack', 'King', 'M', '1818 Cedar St.', '5551000021', 'jack.king@usaexample.com', 1, 5500),
('Amelia', 'Scott', 'F', '1919 Cherry St.', '5551000022', 'amelia.scott@usaexample.com', 2, 6500),
('Elijah', 'Green', 'M', '2020 Ash St.', '5551000023', 'elijah.green@usaexample.com', 3, 7500),
('Zoe', 'Adams', 'F', '2121 Elm St.', '5551000024', 'zoe.adams@usaexample.com', 4, 8500),
('Jack', 'Baker', 'M', '2222 Maple St.', '5551000025', 'jack.baker@usaexample.com', 5, 9500),
('Madison', 'Gonzalez', 'F', '2323 Oak St.', '5551000026', 'madison.gonzalez@usaexample.com', 6, 10500),
('Lucas', 'Nelson', 'M', '2424 Pine St.', '5551000027', 'lucas.nelson@usaexample.com', 7, 11500),
('Charlotte', 'Carter', 'F', '2525 Birch St.', '5551000028', 'charlotte.carter@usaexample.com', 8, 12500),
('Henry', 'Mitchell', 'M', '2626 Cedar St.', '5551000029', 'henry.mitchell@usaexample.com', 9, 13500),
('Amos', 'Perez', 'M', '2727 Cherry St.', '5551000030', 'amos.perez@usaexample.com', 10, 14500),
('Maya', 'Roberts', 'F', '2828 Ash St.', '5551000031', 'maya.roberts@usaexample.com', 1, 5500),
('Ryan', 'Lopez', 'M', '2929 Elm St.', '5551000032', 'ryan.lopez@usaexample.com', 2, 6500),
('Ella', 'Martinez', 'F', '3030 Maple St.', '5551000033', 'ella.martinez@usaexample.com', 3, 7500),
('Nathan', 'Gonzalez', 'M', '3131 Oak St.', '5551000034', 'nathan.gonzalez@usaexample.com', 4, 8500),
('Hailey', 'Lee', 'F', '3232 Pine St.', '5551000035', 'hailey.lee@usaexample.com', 5, 9500),
('Matthew', 'Taylor', 'M', '3333 Birch St.', '5551000036', 'matthew.taylor@usaexample.com', 6, 10500),
('Grace', 'Anderson', 'F', '3434 Cedar St.', '5551000037', 'grace.anderson@usaexample.com', 7, 11500),
('Samuel', 'Thomas', 'M', '3535 Cherry St.', '5551000038', 'samuel.thomas@usaexample.com', 8, 12500),
('Victoria', 'Clark', 'F', '3636 Ash St.', '5551000039', 'victoria.clark@usaexample.com', 9, 13500),
('Owen', 'Harris', 'M', '3737 Elm St.', '5551000040', 'owen.harris@usaexample.com', 10, 14500),
('Nora', 'Roberts', 'F', '3838 Maple St.', '5551000041', 'nora.roberts@usaexample.com', 1, 5500),
('Elena', 'Moore', 'F', '3939 Oak St.', '5551000042', 'elena.moore@usaexample.com', 2, 6500),
('Jordan', 'Jackson', 'M', '4040 Pine St.', '5551000043', 'jordan.jackson@usaexample.com', 3, 7500),
('Aidan', 'Martinez', 'M', '4141 Birch St.', '5551000044', 'aidan.martinez@usaexample.com', 4, 8500),
('Carter', 'Lee', 'M', '4242 Cedar St.', '5551000045', 'carter.lee@usaexample.com', 5, 9500),
('Charlotte', 'Wilson', 'F', '4343 Cherry St.', '5551000046', 'charlotte.wilson@usaexample.com', 6, 10500),
('Evelyn', 'Davis', 'F', '4444 Ash St.', '5551000047', 'evelyn.davis@usaexample.com', 7, 11500),
('Isaac', 'Harris', 'M', '4545 Elm St.', '5551000048', 'isaac.harris@usaexample.com', 8, 12500),
('Megan', 'Lopez', 'F', '4646 Maple St.', '5551000049', 'megan.lopez@usaexample.com', 9, 13500),
('Jackson', 'Moore', 'M', '4747 Oak St.', '5551000050', 'jackson.moore@usaexample.com', 10, 14500),
('Abigail', 'Taylor', 'F', '4848 Pine St.', '5551000051', 'abigail.taylor@usaexample.com', 1, 5500),
('David', 'Scott', 'M', '4949 Birch St.', '5551000052', 'david.scott@usaexample.com', 2, 6500),
('Charlotte', 'Martin', 'F', '5050 Cedar St.', '5551000053', 'charlotte.martin@usaexample.com', 3, 7500),
('Liam', 'Walker', 'M', '5151 Cherry St.', '5551000054', 'liam.walker@usaexample.com', 4, 8500),
('Harper', 'Moore', 'F', '5252 Ash St.', '5551000055', 'harper.moore@usaexample.com', 5, 9500),
('Lucas', 'Taylor', 'M', '5353 Elm St.', '5551000056', 'lucas.taylor@usaexample.com', 6, 10500),
('Gabriel', 'Thomas', 'M', '5454 Maple St.', '5551000057', 'gabriel.thomas@usaexample.com', 7, 11500),
('Zoey', 'Harris', 'F', '5555 Oak St.', '5551000058', 'zoey.harris@usaexample.com', 8, 12500),
('Evan', 'Walker', 'M', '5656 Pine St.', '5551000059', 'evan.walker@usaexample.com', 9, 13500),
('Benjamin', 'Scott', 'M', '5757 Birch St.', '5551000060', 'benjamin.scott@usaexample.com', 10, 14500),
('Ahmed', 'Al-Farsi', 'M', '12 Arabian St.', '0501234568', 'ahmed.al-farsi@arabexample.com', 1, 5000),
('Sara', 'Al-Amiri', 'F', '23 Arabian St.', '0502345679', 'sara.al-amiri@arabexample.com', 2, 6000),
('Mohamed', 'Al-Mansoori', 'M', '34 Arabian St.', '0503456790', 'mohamed.al-mansoori@arabexample.com', 3, 7000),
('Layla', 'Al-Harbi', 'F', '45 Arabian St.', '0504567901', 'layla.al-harbi@arabexample.com', 4, 8000),
('Omar', 'Al-Khalifa', 'M', '56 Arabian St.', '0505679012', 'omar.al-khalifa@arabexample.com', 5, 9000),
('Fatima', 'Al-Jaber', 'F', '67 Arabian St.', '0506789012', 'fatima.al-jaber@arabexample.com', 6, 10000),
('Ali', 'Al-Saleh', 'M', '78 Arabian St.', '0507890123', 'ali.al-saleh@arabexample.com', 7, 11000),
('Mona', 'Al-Shammari', 'F', '89 Arabian St.', '0508901234', 'mona.al-shammari@arabexample.com', 8, 12000),
('Khaled', 'Al-Bakri', 'M', '90 Arabian St.', '0509012345', 'khaled.al-bakri@arabexample.com', 9, 13000),
('Hassan', 'Al-Rashid', 'M', '101 Arabian St.', '0500123456', 'hassan.al-rashid@arabexample.com', 10, 14000),
('Amin', 'Al-Dosari', 'M', '112 Arabian St.', '0501234567', 'amin.al-dosari@arabexample.com', 1, 15000),
('Zainab', 'Al-Banna', 'F', '123 Arabian St.', '0502345678', 'zainab.al-banna@arabexample.com', 2, 5500),
('Samir', 'Al-Mahmoud', 'M', '134 Arabian St.', '0503456789', 'samir.al-mahmoud@arabexample.com', 3, 6500),
('Rania', 'Al-Sabah', 'F', '145 Arabian St.', '0504567890', 'rania.al-sabah@arabexample.com', 4, 7500),
('Tariq', 'Al-Basri', 'M', '156 Arabian St.', '0505678901', 'tariq.al-basri@arabexample.com', 5, 8500),
('Lina', 'Al-Qadi', 'F', '167 Arabian St.', '0506789013', 'lina.al-qadi@arabexample.com', 6, 9500),
('Noor', 'Al-Amin', 'F', '178 Arabian St.', '0507890124', 'noor.al-amin@arabexample.com', 7, 10500),
('Rami', 'Al-Mufti', 'M', '189 Arabian St.', '0508901235', 'rami.al-mufti@arabexample.com', 8, 11500),
('Nadia', 'Al-Hussain', 'F', '190 Arabian St.', '0509012346', 'nadia.al-hussain@arabexample.com', 9, 12500),
('Lina', 'Al-Riyahi', 'F', '201 Arabian St.', '0500123457', 'lina.al-riyahi@arabexample.com', 10, 13500),
('Li', 'Wei', 'M', '123 Chang St.', '5553000001', 'li.wei@asiaexample.com', 1, 5500),
('Siti', 'Zahra', 'F', '456 Bao St.', '5553000002', 'siti.zahra@asiaexample.com', 2, 6500),
('Yuki', 'Tanaka', 'M', '789 Feng St.', '5553000003', 'yuki.tanaka@asiaexample.com', 3, 7500),
('Priya', 'Sharma', 'F', '101 Kyoto St.', '5553000004', 'priya.sharma@asiaexample.com', 4, 8500),
('Sung', 'Kim', 'M', '202 Tokyo St.', '5553000005', 'sung.kim@asiaexample.com', 5, 9500),
('Ming', 'Li', 'M', '303 Beijing St.', '5553000006', 'ming.li@asiaexample.com', 6, 10500),
('Ravi', 'Patel', 'M', '404 Bangalore St.', '5553000007', 'ravi.patel@asiaexample.com', 7, 11500),
('Aisha', 'Hassan', 'F', '505 Dubai St.', '5553000008', 'aisha.hassan@asiaexample.com', 8, 12500),
('Jin', 'Zhao', 'M', '606 Seoul St.', '5553000009', 'jin.zhao@asiaexample.com', 9, 13500),
('Yara', 'Abadi', 'F', '707 Singapore St.', '5553000010', 'yara.abadi@asiaexample.com', 10, 14500),
('Hiroshi', 'Nakamura', 'M', '808 Osaka St.', '5553000011', 'hiroshi.nakamura@asiaexample.com', 1, 5500),
('Anjali', 'Verma', 'F', '909 Mumbai St.', '5553000012', 'anjali.verma@asiaexample.com', 2, 6500),
('Tariq', 'Ahmed', 'M', '1000 Karachi St.', '5553000013', 'tariq.ahmed@asiaexample.com', 3, 7500),
('Jia', 'Chen', 'F', '1111 Hong Kong St.', '5553000014', 'jia.chen@asiaexample.com', 4, 8500),
('Kaito', 'Yamada', 'M', '1212 Fukuoka St.', '5553000015', 'kaito.yamada@asiaexample.com', 5, 9500),
('Rani', 'Kumar', 'F', '1313 Kolkata St.', '5553000016', 'rani.kumar@asiaexample.com', 6, 10500),
('Zhang', 'Wei', 'M', '1414 Shenzhen St.', '5553000017', 'zhang.wei@asiaexample.com', 7, 11500),
('Sara', 'Iqbal', 'F', '1515 Lahore St.', '5553000018', 'sara.iqbal@asiaexample.com', 8, 12500),
('Tomo', 'Sato', 'M', '1616 Kyoto St.', '5553000019', 'tomo.sato@asiaexample.com', 9, 13500),
('Nina', 'Ali', 'F', '1717 Beirut St.', '5553000020', 'nina.ali@asiaexample.com', 10, 14500);
