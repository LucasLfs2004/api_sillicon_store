use sillicon_store;

INSERT INTO product(id, owner, name, description, brand, price, stock, active, created_at, updated_at, category, featured) 
		VALUES ('12345678', 
				3910786717, 
				'Placa de Vídeo RTX 4060', 
				'Placa de Vídeo RTX 4060 8GB de VRAM, excelente para jogos', 
				'Gigabyte',
				1999.99, 
				10,
				true,
				'2023-01-01',
				'2023-01-01',
				'notebook',
				true);
                select * from product; 

INSERT INTO person (id, name, cpf, email, nascimento, telefone, senha) VALUES (0, 'Lucas Ferreira Silva', '520.945.658-74', 'lucas.lfs2004@gmail.com', '2004-06-19', '(11) 97968-4799', 'GallardoLP-570');

select * from category;
select * from person;
select * from image;