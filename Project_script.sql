USE bank_full;

SELECT * FROM bank_full;

ALTER TABLE bank_full
ADD COLUMN client_id INT AUTO_INCREMENT PRIMARY KEY FIRST;

CREATE TABLE client (
client_id int AUTO_INCREMENT,
age int not null,
job varchar(20),
marital_status varchar(20),
education varchar(20),
PRIMARY KEY (client_id),
FOREIGN KEY (client_id) REFERENCES bank_full(client_id)
);

CREATE TABLE account_info (
client_id INT not null,
balance INT,
personal_loan varchar(4),
housing varchar(4),
`default` varchar(3),
PRIMARY KEY (client_id),
FOREIGN KEY (client_id) REFERENCES bank_full(client_id)
);

CREATE TABLE campaign (
client_id INT not null,
contact varchar(20),
day INT,
month varchar(10),
duration INT,
number_of_contacts INT,
pdays INT,
previous INT,
poutcome varchar(10),
PRIMARY KEY (client_id),
FOREIGN KEY (client_id) REFERENCES bank_full(client_id)
);

ALTER TABLE campaign ADD y VARCHAR(100);

INSERT INTO campaign (
    client_id,
    contact,
    day,
    month,
    duration,
    number_of_contacts,
    pdays,
    previous,
    poutcome,
    y
)
SELECT
	client_id,
    contact,
    day,
    month,
    duration,
    campaign,
    pdays,
    previous,
    poutcome,
    y
FROM bank_full;

INSERT INTO campaign y
SELECT y
FROM bank_full;

INSERT INTO client (
    client_id,
    age,
    job,
    marital_status,
    education
)
SELECT
	client_id,
    age,
    job,
    marital,
    education
FROM bank_full;

INSERT INTO account_info (
    client_id,
    balance,
    personal_loan,
    housing,
    `default`
)
SELECT
    client_id,
    balance,
    loan,
    housing,
    `default`
FROM bank_full;