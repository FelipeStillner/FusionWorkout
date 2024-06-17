INSERT INTO public."User"(
	email, name, password, kind)
	VALUES ('c@c.com', 'c', 'c', 'C'),
	('p@p.com', 'p', 'p', 'P'),
	('m@m.com', 'm', 'm', 'M');
	
INSERT INTO public."Client"(
	id, "weight (Kg)", "height (cm)", sex)
	VALUES (1, 90, 180, 'M');
	
INSERT INTO public."Manager"(
	id)
	VALUES (3);
	
INSERT INTO public."Personal"(
	id, manager_id)
	VALUES (2, 3);
	
INSERT INTO public."Food"(
	client_id, day, name, "quantity (g)", "energy (cal)")
	VALUES (1, 0, 'd0-f0', 5, 6),
	(1, 0, 'd0-f1', 6, 7),
	(1, 0, 'd0-f2', 7, 8),
	(1, 1, 'd1-f3', 8, 9),
	(1, 1, 'd1-f4', 9, 10),
	(1, 2, 'd2-f5', 10, 11);
	
INSERT INTO public."Circuit"(
	client_id, day, name, repetitions)
	VALUES (1, 0, 'd0-c0', 3),
	(1, 0, 'd0-c1', 4),
	(1, 1, 'd1-c2', 5);
	
INSERT INTO public."Workout"(
	circuit_id, name, repetitions, duration)
	VALUES (0, 'c0-w0', 1, '00:02:00'),
	(0, 'c0-w1', 2, '00:03:00'),
	(0, 'c0-w2', 3, '00:04:00'),
	(1, 'c1-w3', 4, '00:05:00'),
	(1, 'c1-w4', 5, '00:06:00'),
	(1, 'c1-w5', 6, '00:07:00'),
	(2, 'c2-w6', 7, '00:08:00'),
	(2, 'c2-w7', 8, '00:09:00'),
	(2, 'c2-w8', 9, '00:10:00');

INSERT INTO public."Appointment"(
	client_id, date, personal_id, "time")
	VALUES (NULL, '01-01-2024', 2, '11:35'),
	(1, '01-01-2024', 2, '11:40');