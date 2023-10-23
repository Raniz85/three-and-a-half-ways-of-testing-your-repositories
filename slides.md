---
theme: ./theme

# https://sli.dev/custom/highlighters.html
highlighter: shiki

# show line numbers in code blocks
lineNumbers: false

# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)

# persist drawings in exports and build
drawings:
  persist: false

# use UnoCSS
css: unocss

layout: intro
---

# Three-and-a-half Ways of Testing Your Repositories

Daniel Raniz Raneland<br />
Coding Architect @ factor10

<ul class="list-none! columns-2">
  <li><mdi-email />raniz@factor10.com</li>
  <li><mdi-mastodon />raniz@mastodon.online</li>

  <li><mdi-firefox />raniz.blog</li>
  <li><mdi-linkedin />/in/raneland</li>
</ul>

---

# About Raniz

<div class="absolute bottom-0 left-30% mx-auto w-300px">
  <img src="/images/raniz-silhouette.svg" />
</div>

<v-clicks>
  <div speech-bubble pright acenter class="absolute top-400px left-45px w-300px" style="--bbPadding: 0.5rem">
    <img src="/images/Lund_university_L_CMYK.svg" />
  </div>
  <div speech-bubble pbottom aright class="absolute top-240px left-100px">
    <img src="/images/sony-logo.svg" class="h-30px float-left"/><span class="ml-2 text-size-20px">東京</span>
  </div>
  <div speech-bubble pbottom aright class="absolute top-110px left-290px">
    <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[120px] h-auto md:w-[118px]" viewBox="0 0 357 179" width="118" height="59"><path fill="currentColor" fill-rule="evenodd" d="M283.7.4 282 3.7a96.6 96.6 0 0 1-14 19.5c-5 5.6-9.5 10.4-17.6 18.5-5 5-11 11.2-13.4 13.8l-4.4 4.7v1.4c0 4 3.5 11.7 5.2 11.7.3 0 .8-.2 1.2-.5a52.6 52.6 0 0 0 13-10l2.2-2c2.7-2.6 2.7-2.6 1 2.5a310.7 310.7 0 0 0-3 9.5 672.4 672.4 0 0 0-9.8 36.2l-.5 2a43 43 0 0 0-.8 4.1 189.4 189.4 0 0 0-4 48.9c.6 4.3 1.2 6.5 3 10.2 3.4 6.7 5.9 5.8 5.9-2 0-8 1-21.3 2.5-31.2l1.7-10.1A384.7 384.7 0 0 1 266 72.2a427.5 427.5 0 0 1 10.2-24.6c1-2.5 5.9-12 7.4-14.8l2-3.7a25.2 25.2 0 0 1 1.6-2.6l.7-1.2c4-5.7 4.6-9.9 2.4-15l-.7-2c-2.3-6.2-4.8-9.5-5.8-7.9ZM321.3 13c-9.7 1.8-20.6 12.9-30.6 31a149.8 149.8 0 0 0-12 29.9 205.8 205.8 0 0 0-4.4 17.5l-.5 2.6a234.6 234.6 0 0 0-2.3 14.3 108.3 108.3 0 0 0 3 38.3c6.7 23.2 20 33.8 35.2 27.9 12.4-5 21-14.8 30.4-35.2a49.2 49.2 0 0 0 1.8-3.8 198.3 198.3 0 0 0 12.5-43 146.3 146.3 0 0 0 1.1-42.1 66 66 0 0 0-2.1-9.5 45 45 0 0 0-9.4-18.5 18.7 18.7 0 0 0-4.6-3.6l-1.8-1.3c-5.7-4.2-10.7-5.6-16.3-4.5Zm13.4 17.4c2.6.6 3.2.8 3.7 1.6.8 1 1 1.2 2.1 1.8 5.2 2.6 6.2 4.4 7 11.4 1.5 16.3-5.4 49.8-14.6 70.3l-1 2a118 118 0 0 1-13.4 23c-2.9 3.9-9 9-13.4 11.2-20.7 10.2-29.8-5-23.4-39a107.3 107.3 0 0 1 1.4-6.8 283.2 283.2 0 0 1 7.2-25.1 174.9 174.9 0 0 1 12.3-27c9.5-16.5 22.2-25.7 32-23.4ZM19.4 55c-7.2 1.4-11.7 7-12.6 15.8-.3 3.1 0 2.8-3.7 3H0v6.8h3.3l3.3.1v39H15v-19.2c0-10.6 0-19.3.2-19.5.1-.2 1.4-.3 4.7-.4h4.5v-6.7l-4.6-.1-4.7-.2c-.6-1 0-5 .9-7.1 1.9-4.2 7.3-6.3 11.2-4.4.5.3 1.1 0 1.1-.4l1.2-3.3c.7-1.6.8-2 .7-2.2a28 28 0 0 0-10.7-1.1Zm105.9 6.5a284.6 284.6 0 0 1-6.2 2.5c-.2.1-.3 1.4-.3 4.8 0 5.3.3 4.9-3 4.9h-2.5v6.4h2.7l2.7.1.1 14.7c.1 9.4.3 15 .4 15.5 2.7 8.6 8.8 11.6 20.1 9.7 4-.7 3.9-.6 3.4-2.9a61 61 0 0 1-.9-4.8c0-.2-.8 0-2.1.4-4.1 1.3-8.4.8-10.2-1.2-2.4-2.6-2.6-4.7-2.5-20V80.3h6.3l6.3-.1v-6.4h-6a77 77 0 0 1-6.3-.2c-.3-.1-.4-.9-.4-6.3 0-4.8 0-6.2-.3-6.1l-1.3.4ZM43.9 73c-4.1.6-9.3 2.5-11.3 4l-.6.5 1.7 3.4c1.2 2.2 1.8 3.3 2 3.2.2 0 1-.7 2-1.3a16.8 16.8 0 0 1 14.8-1.4c2.5 1.2 4 3.6 4.6 7.3.4 2.3.3 2.6-1 2.2-9-2.3-19.4 1.3-24 8.1a14.1 14.1 0 0 0 4 19.8c6 3.5 16.5 2 21.2-3.2.8-.8.8-.8 1.3.3 1.5 3 3.8 4.4 8.4 4.7l2 .2v-4.3l-1-.9a9 9 0 0 1-1.6-2.3l-.6-1.3-.2-11.9c-.2-16.3-.8-19-5-23-3.1-3-11.1-5-16.7-4.1Zm49.5 0a27.8 27.8 0 0 0-9.3 2.4 23 23 0 0 0-4.7 3.6c-10.4 10-9.4 30 2 38 7 4.7 18.3 5 27 .6 2.2-1.1 2.2-1 1-3.5l-1.5-3.2c-.7-1.4-.7-1.5-1.8-.8a17.4 17.4 0 0 1-16 2.7c-12.3-4.3-12.2-27 .1-32 4-1.6 11.5-.7 15 1.8 1 .7 1.2.6 3.3-2.3l2-2.7-1-.7a27.7 27.7 0 0 0-16-4Zm69.2 0c-8 1-13.2 5.3-16.6 13.3a35.6 35.6 0 0 0-.3 20.4c.5 2.2 3 6.5 5.2 8.6a21.5 21.5 0 0 0 28.9-.2c9.2-9.4 8.4-30.6-1.4-38.2a23 23 0 0 0-15.8-4Zm48.4 0c-3.7.7-7.3 3-9.3 6-1 1.6-1.1 1.4-1.1-2.2v-3h-8.3v46h8.3v-14.4c0-16 0-16 1.7-19.3 3-5.9 8.5-7.6 14.3-4.5.2 0 .5-.5 2.2-4.6l1.2-3.3c-.6-.5-7-1-9-.6Zm-42 7.3a9 9 0 0 1 4.2 2.5c5.6 5.8 5.6 21.4 0 27.7a11.2 11.2 0 0 1-18-2c-2.9-5.6-3-16.3-.1-22.1 2.7-5.4 8.4-7.9 13.9-6ZM53.8 96.7c4 .6 3.5-.1 3.5 6.3v5.3l-1.5 1.5c-8.3 8.2-21 4-17.3-5.9 1.9-5 8.8-8.2 15.3-7.2Z" clip-rule="evenodd"></path></svg>
  </div>
  <div speech-bubble pbottom aleft class="absolute top-130px left-520px">
    <span class="text-size-250%">&#x1F470;&#x200D;&#x2640;&#xFE0F; <!-- woman with veil --></span>
    <span class="text-size-175%">
      &#x1F467; <!-- girl -->
      &#x1F466; <!-- boy -->
    </span>
  </div>
  <div speech-bubble pbottom aleft class="absolute top-285px left-590px text-size-250%">
    &#x1F37A;
  </div>
  <div speech-bubble pleft acenter class="absolute bottom-15px right-100px h-80px" style="--bbPadding: 0.2rem">
    <img src="/images/triathlon.png" class="w-full h-full"/>
  </div>

</v-clicks>

---
layout: image-right
image: /images/Domain_Driven_Design-EricEvans.jpg
---

# Domain Driven Design

- Divide the business into _boundedDALL·E 2023-10-21 13.45.06 - Illustration in anime style displaying an expansive view of a university lecture hall. The bearded male software developer is seen from afar, gesturin contexts_
- Focus on the core _domain_ of each bounded context and it's logic
- Ongoing collaboration with domain experts
- Model software after the domain, using the same language
- Multi-layered architecture

---

# Layers in Domain Driven Design

<img src="/images/ddd-layers.svg" class="max-h-420px"/>

<div v-click class="absolute bottom-150px left-50px color-red">
  <img src="/images/highlight-circle.svg" width="120" height="100"/>
</div>

---

# Two Types of Developers

<div class="columns-2">

<div v-click>
  <h2>Runs Away</h2>
  <img src="/images/developer-running-away.png" />
</div>
<div v-click>
  <h2>Gets Down To Work</h2>
  <img src="/images/developer-focusing.png" />
</div>

</div>

---

# Makes a Presentation About It

<p></p>

![](/images/developer-presenting.png)

---
layout: cover
background: /images/cinnamon-buns.jpg
---

<div class="attribution">
  License: CC BY-SA 2.0, https://www.flickr.com/photos/infomastern/
</div>

---

# Basic Architecture

<img src="/images/testing-interceptions-Baseline.png"/>

---

# Repositories

<div v-click class="absolute left-320px top-50px">
  <img class="mx-auto" src="/images/Amazon-S3-Logo.svg" width="150" />
  S3PastryRepository
</div>

<div v-click class="absolute left-20px top-230px">
  <img class="mx-auto" src="/images/DynamoDB.png" width="150" />
  DynamoDbPastryRepository
</div>

<div v-click class="absolute right-200px bottom-30px">
  <img class="mx-auto" src="/images/Postgresql_elephant.svg" width="150" />
  JdbcPastryRepository
</div>

---

# Workflow

<v-clicks depth="2">

- Test Driven Development
- Gherkin (from Behaviour Driven Development)
    * Given
    * When
    * Then
 
</v-clicks>

---

<h1>Mocking the Client <img class="inline-block" src="/images/Amazon-S3-Logo.svg" width="25"/></h1>

<p></p>

![](/images/testing-interceptions-Mock.png)

---

<SlidevVideo controls>
  <source src="/videos/coding-s3.mp4" controls />
</SlidevVideo>

---

# Mocking the Client

## Advantages
- Fast
- Test setup is usually easier than other methods

## Drawbacks
- More mocking means higher test complexity
- Tightly tied to implementation
- Configuring mocks produces noise
- Test data probably needs to be hand-crafted in code


---

# When to Mock the Client
- Simple API
- Straightforward mocking process

---

<h1>Mocking the Service <img class="inline-block" src="/images/DynamoDB.png" width="50" /></h1>

<p></p>

![](/images/testing-interceptions-MockServer.png)

---

<video src="videos/coding-dynamodb.mp4" controls />

---

# Mocking the Service

## Advantages

- Client library code is still executed
- (Probably) Agnostic to client implementation
- Test data can easily be collected from real environment

## Drawbacks

- Slight increase in startup time
- Request mocking produces noise

---

# When to Mock the Service
- REST APIs
- Client does transforms/computations
- Setup is easier than mocking the client

---
layout: center
---

# What About non-HTTP Services?

<v-clicks>

```java
try (var connection = dataSource.getConnection();
     var statement = connection.createStatement()) {
    statement.execute("INSERT INTO pastries (type, amount) VALUES ('Cinnamon Bun', 24)");
}
```

</v-clicks>


---

# Mocking JDBC

```java
@Test
void thatStoringPastryInsertsIt() throws IOException, SQLException {
    // Given a pastry repository with a mocked datasource
    when(dataSource.getConnection())
            .thenReturn(connection);
    when(connection.createStatement())
            .thenReturn(statement);
    var repo = new JdbcPastryRepository(dataSource);
    
    // and a pastry to store
    var pastry = new Pastry("Cinnamon Bun", 24);

    // when the pastry is stored in the repository
    repo.store(pastry);

    // then a row with 24 cinnamon rolls is stored in the database
    verify(statement).execute("INSERT INTO pastries (type, amount) VALUES ('Cinnamon Bun', 24)");
}
```

---
clicks: 4
---

# Refactorings

<ul>
<li v-click="1">
 Quoting

  ```sql
  INSERT INTO "pastries" ("type", "amount") VALUES ('Cinnamon Bun', 24);
  ```

  <div v-click="2" class="mt-1">

  ```
  Argument(s) are different! Wanted:
  statement.execute(
      "INSERT INTO pastries (type, amount) VALUES ('Cinnamon Bun', 24)"
  );
  -> at repos.MockJdbcPastryRepositoryTest.testStorePastry(MockJdbcPastryRepositoryTest.java:46)
  Actual invocations have different arguments:
  statement.execute(
      "INSERT INTO "pastries" ("type", "amount") VALUES ('Cinnamon Bun', 24)"
  )
  ```
  
  </div>
</li>
<li v-click="3"><em>PreparedStatement</em>

  ```java
  var statement = connection.prepareStatement("INSERT INTO pastries (type, amount) VALUES (?, ?)"));
  statement.setString(1, pastry.type());
  statement.setInt(2, pastry.amount());
  statement.execute();
  ```

  <div v-click="4" class="mt-1">

  ```
  java.lang.NullPointerException: Cannot invoke "java.sql.PreparedStatement.setString(int, String)" because "statement" is null
  ```

  </div>
</li>
</ul>
  

---
layout: statement
---

# Asserting Exact SQL Statements Is Brittle

---

<h1>Verifying Against The Real Service <img class="inline-block" src="/images/Postgresql_elephant.svg" width="50"/></h1>

<p></p>

![](/images/testing-interceptions-Service.png)

---

<video src="/videos/coding-postgres-local.mp4" controls />

---

# Verifying Against a Real Service

## Advantages
- As close to production environment as possible
- Testing remains simple regardless of query complexity
- Test data can be collected from real environment
- Little or no impact on startup time

## Drawbacks
- Needs cleanup, which can (and will) fail to clean up everything
- Needs external resources to be available

---

# No Cleanup => Test Databases Left Behind

```java
@BeforeEach
void setUpDataSource() throws SQLException {
    dataSource = new PGSimpleDataSource();
    dataSource.setDatabaseName("postgres");
    var dbName = "test_db_" + System.nanoTime();
    try (var connection = dataSource.getConnection();
        var statement = connection.createStatement()) {
        statement.execute("CREATE DATABASE " + dbName);
    }
    dataSource.setDatabaseName(dbName);
}
```

---

# No Cleanup => Test Databases Left Behind

```java
@AfterEach
void cleanUpTestDatabase() throws SQLException {
    dataSource.setDatabaseName("postgres");
    try (var connection = dataSource.getConnection();
        var statement = connection.createStatement()) {
        statement.execute("DROP DATABASE " + dbName);
    }
}
```

---

# When to Use Real Services

- When there is no other alternative

---

<h1>Verifying Against a Temporary Service <img class="inline-block" src="/images/Postgresql_elephant.svg" width="50"/></h1>

<p></p>

![](/images/testing-interceptions-Container.png)

---

<video src="/videos/coding-postgres-container.mp4" controls />

---

# Verifying Against a Temporary Service

## Advantages
- Very close to production environment
- Testing remains simple regardless of query complexity
- Test data can be collected from real environment

## Drawbacks
- Increased startup time

<!--
 Postgres container starts in about a second
-->

---

# When to Use Temporary Services

- As often as possible
- When the other techniques don't give you confidence

---
layout: center
---

# Three-and-a-half Ways of Testing Your Repositories

<ul class="!list-none">
  <li v-click><span class="inline-block min-w-2em">1)</span> Mocking the service</li>
  <li v-click><span class="inline-block min-w-2em">2)</span> Mocking the client</li>
  <li v-click><span class="inline-block min-w-2em">3)</span> Verifying against a temporary service</li>
  <li v-click><span class="inline-block min-w-2em">3.5)</span> Verifying against a persistent service</li>
</ul>

---

# Mocking the Client

## Advantages
- Fast
- Test setup is usually easier than other methods

## Drawbacks
- More mocking means higher test complexity
- Tightly tied to implementation
- Configuring mocks produces noise
- Test data probably needs to be hand-crafted in code

---

# Mocking the Service

## Advantages
- Client library code is still executed
- (Probably) Agnostic to client implementation
- Test data can easily be collected from real environment

## Drawbacks
- Slight increase in startup time
- Request mocking produces noise

---

# Verifying Against a Temporary Service

## Advantages
- Very close to production environment
- Testing remains simple regardless of query complexity
- Test data can be collected from real environment

## Drawbacks
- Increased startup time

---

# Verifying Against a Real Service

## Advantages
- As close to production environment as possible
- Testing remains simple regardless of query complexity
- Test data can be collected from real environment
- Little or no impact on startup time

## Drawbacks
- Needs external resources to be available
- Needs cleanup, which can (and will) fail to clean up everything

---

# Technology List
- AssertJ - Fluent assertions in Java
- Mockito - Mocking, stubbing and verifying interactions
- MockServer - Mocking and verifying HTTP(S) services
- TestContainers - Controlling temporary, local services in containers for test and verification

---

# Three-and-a-half Ways of Testing Your Repositories

Daniel Raniz Raneland<br />
Coding Architect @ factor10

<div class="grid grid-cols-2">

  <div>
    <ul class="!list-none">
      <li><span class="inline-block min-w-2em">1)</span> Mocking the service</li>
      <li><span class="inline-block min-w-2em">2)</span> Mocking the client</li>
      <li><span class="inline-block min-w-2em">3)</span> Verifying against a temporary service</li>
      <li><span class="inline-block min-w-2em">3.5)</span> Verifying against a persistent service</li>
    </ul>
  </div>

  <div>
    <ul class="list-none!">
      <li><mdi-email />raniz@factor10.com</li>
      <li><mdi-mastodon />raniz@mastodon.online</li>
      <li><mdi-firefox />raniz.blog</li>
      <li><mdi-linkedin />/in/raneland</li>
    </ul>
    <img src="/images/linkedin-qr.png" width="250"/>
  </div>

</div>

