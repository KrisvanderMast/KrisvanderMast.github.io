---
layout: post
title: "Making use of the Idempotent flag when generating scripts with Entity Framework Core"
date: 2019-03-08 13:41:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["entity framework core", "migrations", "sql"]
author: Kris van der Mast
---
Today I was setting up a new project but was making use of Entity Framework Core. Seems I found an interesting flag -Idempotent to generate SQL statements from all the generated migrations.  
The command itself to be used in Visual Studio Package Manager Console goes as follows:
> Script-Migration -Idempotent

Why I found it interesting is because I spent a lot of time with Entity Framework 6 last year on a difficult project where I was involved in drastically improving the performance of the application. It involved doing a lot of migrations. I was on a separate branch though for weeks while the rest of the team was regularly adding new code to the master branch (coming from feature branches with pull requests). They luckily only added 1 migration themselves but it kept hauting me. I also asked it during some job interviews when looking for a new client enf of last year while I was sparring with the architecture teams but none had thought about the scenario.

Given the following code in C#:

```csharp
public class BloggingContext : DbContext
{
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer(@"Server=(localdb)\mssqllocaldb;Database=EFGetStarted.ConsoleApp.NewDb;Trusted_Connection=True;");
    }
}
```

```csharp
public class Blog
{
    public int BlogId { get; set; }
    public string Url { get; set; }

    // Relations
    public List<Post> Posts { get; set; }
}
```

```csharp
public class Post
{
    public int PostId { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }

    // Relations
    public int BlogId { get; set; }
    public Blog Blog { get; set; }
}
```

When you run the following script to generate the SQL statements:

> Script-Migration

You'll get to see the following output:

```sql
IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL
BEGIN
    CREATE TABLE [__EFMigrationsHistory] (
        [MigrationId] nvarchar(150) NOT NULL,
        [ProductVersion] nvarchar(32) NOT NULL,
        CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
    );
END;

GO

CREATE TABLE [Blogs] (
    [BlogId] int NOT NULL IDENTITY,
    [Url] nvarchar(max) NULL,
    CONSTRAINT [PK_Blogs] PRIMARY KEY ([BlogId])
);

GO

CREATE TABLE [Posts] (
    [PostId] int NOT NULL IDENTITY,
    [Title] nvarchar(max) NULL,
    [Content] nvarchar(max) NULL,
    [BlogId] int NOT NULL,
    CONSTRAINT [PK_Posts] PRIMARY KEY ([PostId]),
    CONSTRAINT [FK_Posts_Blogs_BlogId] FOREIGN KEY ([BlogId]) REFERENCES [Blogs] ([BlogId]) ON DELETE CASCADE
);

GO

CREATE INDEX [IX_Posts_BlogId] ON [Posts] ([BlogId]);

GO

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20190308092538_InitialCreate', N'2.2.2-servicing-10034');

GO
```

When using
> Script-Migration -Idempotent

The output becomes:

```sql
IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL
BEGIN
    CREATE TABLE [__EFMigrationsHistory] (
        [MigrationId] nvarchar(150) NOT NULL,
        [ProductVersion] nvarchar(32) NOT NULL,
        CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
    );
END;

GO

IF NOT EXISTS(SELECT * FROM [__EFMigrationsHistory] WHERE [MigrationId] = N'20190308092538_InitialCreate')
BEGIN
    CREATE TABLE [Blogs] (
        [BlogId] int NOT NULL IDENTITY,
        [Url] nvarchar(max) NULL,
        CONSTRAINT [PK_Blogs] PRIMARY KEY ([BlogId])
    );
END;

GO

IF NOT EXISTS(SELECT * FROM [__EFMigrationsHistory] WHERE [MigrationId] = N'20190308092538_InitialCreate')
BEGIN
    CREATE TABLE [Posts] (
        [PostId] int NOT NULL IDENTITY,
        [Title] nvarchar(max) NULL,
        [Content] nvarchar(max) NULL,
        [BlogId] int NOT NULL,
        CONSTRAINT [PK_Posts] PRIMARY KEY ([PostId]),
        CONSTRAINT [FK_Posts_Blogs_BlogId] FOREIGN KEY ([BlogId]) REFERENCES [Blogs] ([BlogId]) ON DELETE CASCADE
    );
END;

GO

IF NOT EXISTS(SELECT * FROM [__EFMigrationsHistory] WHERE [MigrationId] = N'20190308092538_InitialCreate')
BEGIN
    CREATE INDEX [IX_Posts_BlogId] ON [Posts] ([BlogId]);
END;

GO

IF NOT EXISTS(SELECT * FROM [__EFMigrationsHistory] WHERE [MigrationId] = N'20190308092538_InitialCreate')
BEGIN
    INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
    VALUES (N'20190308092538_InitialCreate', N'2.2.2-servicing-10034');
END;

GO
```

I'm going to try this further the coming weeks when the current team I'm in will be upstaffing and see what gives.

If this got you triggered you might be interested in reading more about it in the [documentation](https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/powershell#script-migration).

Kris.