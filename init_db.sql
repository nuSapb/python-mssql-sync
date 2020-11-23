
TestId
,Station
,Operator
,FamilyName
,FixtureId
,FixtureSerialNumber
,ProjectRevision
,ProjectReleased
,VariantCode
,VariantReleased
,EC
,Socket
,DateTime
,StatusId
,FailureCode
,FailureDescription
,ErrorCode
,ErrorDescription
,ExecutionTime

CREATE TABLE UUTResults
(
    TestId nvarchar (255) PRIMARY KEY NOT NULL,
    StatusId int NOT NULL,
    --UUTResultsId int NOT NULL,
    StationId int NOT NULL,
    OperatorId int,
    FamilyId int NOT NULL,
    FixtureId nvarchar(50),
    ProjectRevision nvarchar(255) NOT NULL,
    ProjectReleased bit ,
    VariantId int NOT NULL,
    VariantReleased bit NOT NULL,
    EC nvarchar (50),
    Socket int NOT NULL,
    --SerialNumber nvarchar (255) NOT NULL,
    DateTime DATETIME NOT NULL,
    FailureCode int,
    FailureDescription nvarchar (4000),
    ErrorCode int,
    ErrorDescription nvarchar (4000),
    ExecutionTime FLOAT
);


--VariantDetail
insert  into VariantDetail
    ( VariantId, VariantCode)
values
    (1, '461023280103'),
    (2, '4610234D0201'),
    (3, '461048320301'),
    (4, '4610483J0301'),
    (5, '4610484J0201');

-- clear table (empty)
TRUNCATE TABLE [A123_FCT1_DBSync].[dbo].[UUTResults]
TRUNCATE TABLE [A123_FCT1_DBSync].[dbo].[TestDetail]

-- count duplicated rows
SELECT [UUTResultsId], [SerialNumber], COUNT(*)
FROM [A123_FCT1_DBSync].[dbo].[TestDetail]
GROUP BY [UUTResultsId], [SerialNumber],[DateTime]
HAVING COUNT(*) > 1

-- Show all duplicated rows
SELECT DISTINCT t1.*
FROM [A123_FCT1_DBSync].[dbo].[TestDetail] AS t1
    INNER JOIN [A123_FCT1_DBSync].[dbo].[TestDetail] AS t2
    ON t1.[SerialNumber] = t2.[SerialNumber]
order by t1.[SerialNumber]


CREATE TABLE StepResults
(
    TestId nvarchar(255),
    StepResultsId int,
    SequenceCallStepResultsId int,
    StepName nvarchar(500),
    StepSequence nvarchar(500),
    StepNumber int,
    StepId nvarchar(255),
    LookUpString nvarchar(1000),
    StepTypeName nvarchar(255),
    SequenceFilePath nvarchar(500),
    StatusId int,
    FailureCode int,
    FailureDescription nvarchar(4000),
    ErrorCode int,
    ErrorDescription nvarchar(4000),
    ResultTypeId int,
    BooleanResult bit,
    NumericResult float,
    NumericLimitLow float,
    NumericLimitHigh float,
    NumericComparisonId float,
    NumericUnits nvarchar(50),
    StringResult nvarchar(255),
    StringLimit nvarchar(255),
    StringComparisonId float,
    ExecutionTime float
);

SELECT TOP 0 *
INTO [A123_FCT3_DBSync].[dbo].[UUTresults]
FROM [A123_FCT2_DBSync].[dbo].[UUTresults]



