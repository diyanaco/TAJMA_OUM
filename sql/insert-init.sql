-- Admin user
INSERT into psy_user (
        id,
        firstName,
        lastName,
        email,
        password,
        profPic,
        gender,
        age,
        IC,
        race,
        mobile
    )
VALUES (
        '7fce170a-4813-46d7-ac5e-0399ad4085d1',
        'user',
        'admin',
        'admin@demo.com',
        --change hashed password here
        '$2b$12$zSq2iZYBHDUOinevarjf5.v59lMscvv8AqVqlQODxaoVjHzD.zXvS',
        'admin-prof-pic.jpg',
        'male',
        '30',
        '987654321',
        'inconnu',
        '0123456789'
    );

-- Roles
INSERT into psy_role (id, name, code)
VALUES (
        "6611d9ce-c699-4741-a3e6-f1786cb7cb06",
        "Admin",
        "ADMIN"
    );
INSERT into psy_role (id, name, code)
VALUES (
        "16766962-0a86-44d1-ba81-68af7a3b8fc9",
        "Super Admin",
        "SUPER_ADMIN"
    );
INSERT into psy_role (id, name, code)
VALUES (
        "89a086fd-01ff-4bca-a76a-dbf9c27f30d1",
        "Student",
        "STUDENT"
    );

--User role link
INSERT into psy_user_role_link (id, user_id, role_id)
VALUES(
    "abe0eaa4-6fa0-4cf6-8bcd-18248cdd8b78",
    "7fce170a-4813-46d7-ac5e-0399ad4085d1",
    "6611d9ce-c699-4741-a3e6-f1786cb7cb06"
);
INSERT into psy_user_role_link (id, user_id, role_id)
VALUES(
    "2f25a64b-7f96-4910-8c97-d4496b36fec28",
    "7fce170a-4813-46d7-ac5e-0399ad4085d1",
    "16766962-0a86-44d1-ba81-68af7a3b8fc9"
);
INSERT into psy_user_role_link (id, user_id, role_id)
VALUES(
    "8a1e7db3-2d15-440d-87c3-00150f95542f",
    "7fce170a-4813-46d7-ac5e-0399ad4085d1",
    "89a086fd-01ff-4bca-a76a-dbf9c27f30d1"
);