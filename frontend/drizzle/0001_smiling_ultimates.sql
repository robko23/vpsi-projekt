CREATE TABLE `credentials` (
	`userId` text NOT NULL,
	`passwordHash` text NOT NULL,
	FOREIGN KEY (`userId`) REFERENCES `user`(`id`) ON UPDATE no action ON DELETE cascade
);
