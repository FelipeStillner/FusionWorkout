INSERT INTO public."User"(
	email, name, password, kind)
	VALUES ('c@c.com', 'c', 'c', 'C'),
	('p@p.com', 'p', 'p', 'P'),
	('m@m.com', 'm', 'm', 'M');
	
INSERT INTO public."Client"(
	id, "weight (Kg)", "height (cm)", sex)
	VALUES (10, 90, 180, 'M');
	
INSERT INTO public."Manager"(
	id)
	VALUES (12);
	
INSERT INTO public."Personal"(
	id, manager_id)
	VALUES (11, 12);
	
INSERT INTO public."Food"(
	id, client_id, day, name, "quantity (g)", "energy (cal)")
	VALUES (0, 10, 0, 'd0-f0', 5, 6),
	(1, 10, 0, 'd0-f1', 6, 7),
	(2, 10, 0, 'd0-f2', 7, 8),
	(3, 10, 1, 'd1-f3', 8, 9),
	(4, 10, 1, 'd1-f4', 9, 10),
	(5, 10, 2, 'd2-f5', 10, 11);
	
INSERT INTO public."Circuit"(
	id, client_id, day, name, repetitions)
	VALUES (0, 10, 0, 'd0-c0', 3),
	(1, 10, 0, 'd0-c1', 4),
	(2, 10, 1, 'd1-c2', 5);
	
INSERT INTO public."Workout"(
	id, circuit_id, name, repetitions, duration)
	VALUES (0, 0, 'c0-w0', 1, '00:02:00'),
	(1, 0, 'c0-w1', 2, '00:03:00'),
	(2, 0, 'c0-w2', 3, '00:04:00'),
	(3, 1, 'c1-w3', 4, '00:05:00'),
	(4, 1, 'c1-w4', 5, '00:06:00'),
	(5, 1, 'c1-w5', 6, '00:07:00'),
	(6, 2, 'c2-w6', 7, '00:08:00'),
	(7, 2, 'c2-w7', 8, '00:09:00'),
	(8, 2, 'c2-w8', 9, '00:10:00');