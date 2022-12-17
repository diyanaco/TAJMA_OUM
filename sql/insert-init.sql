-- set variables
SET @password1 ='$2b$12$9wQRma6yMLipV69NslyUTev0UZTsb.IqNfvv0bYk/GkCneM/neUT6';
SET @password2 ='$2b$12$/5jj/Z0Gk1Q/gsIXO2sQaOQHw9Fd2jqMDZcDeEEd6atMFLGPrb.qa';
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
        @password1,
        'admin-prof-pic.jpg',
        'male',
        '30',
        '987654321',
        'inconnu',
        '0123456789'
    ),
    (
        'e8f8ab35-ce89-449e-a5a6-8536c7309607',
        'Hamza Fadhilah',
        'Huinana',
        'counselor@demo.com',
        @password2,
        'counselor-pic.jpg',
        'male',
        '35',
        '432156789',
        'inconnu',
        '0123456789'
    );
-- Roles
INSERT into psy_role (id, name, code)
VALUES (
        "6611d9ce-c699-4741-a3e6-f1786cb7cb06",
        "Admin",
        "ADMIN"
    ),
    (
        "16766962-0a86-44d1-ba81-68af7a3b8fc9",
        "Super Admin",
        "SUPER_ADMIN"
    ),
    (
        "89a086fd-01ff-4bca-a76a-dbf9c27f30d1",
        "Student",
        "STUDENT"
    ),
    (
        "74fb5381-6464-4951-893f-2369a4098496",
        "Counselor",
        "COUNSELOR"
    );
-- User role link
INSERT into psy_user_role_link (id, user_id, role_id)
VALUES(
        "abe0eaa4-6fa0-4cf6-8bcd-18248cdd8b78",
        "7fce170a-4813-46d7-ac5e-0399ad4085d1",
        "6611d9ce-c699-4741-a3e6-f1786cb7cb06"
    ),
    (
        "2f25a64b-7f96-4910-8c97-d4496b36fec28",
        "7fce170a-4813-46d7-ac5e-0399ad4085d1",
        "16766962-0a86-44d1-ba81-68af7a3b8fc9"
    ),
    (
        "8a1e7db3-2d15-440d-87c3-00150f95542f",
        "7fce170a-4813-46d7-ac5e-0399ad4085d1",
        "89a086fd-01ff-4bca-a76a-dbf9c27f30d1"
    ),
    (
        "957e399b-bf59-4f26-82fc-f751bf33d951",
        "e8f8ab35-ce89-449e-a5a6-8536c7309607",
        "74fb5381-6464-4951-893f-2369a4098496"
    );