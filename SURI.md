# SURI Specification Testing

## SURI Overview

- **Codebase**: https://github.com/sul-dlss/suri2/
- **Machine**: `sul-lyberservices-[test|dev|prod].stanford.edu`
- **Location**: `/usr/share/tomcat6/webapps/suri2`
- **State of test / dev / prod machines**: uncertain if deployed codebases are same
- **Oracle databases**: `suldbdev2`, `suldbtest2`, `suldbprod2`
- **Service URL**: http://sul-lyberservices-[test|dev|prod].stanford.edu/suri2/
- **Logs**: `/usr/share/tomcat6/webapps/suri2/WEB-INF/suri2.log`
- **Monitoring**: Nagios (/suri2/namespaces is 200 OK)
- **SURI specification (appears mostly up to date)**: https://consul.stanford.edu/display/chimera/SURI+2.0+Specification
- **SURI endpoints of interest for SDR**:
    - druid namespace: https://sul-lyberservices-prod.stanford.edu/suri2/namespaces/druid
    - mint a DRUID: HTTP/POST to https://sul-lyberservices-prod.stanford.edu/suri2/namespaces/druid/identifiers?quantity=1 with authentication (check `dor-services` shared configs)
    - HTTP/GET request to https://sul-lyberservices-prod.stanford.edu/suri2/namespaces/druid/identifiers should return all DRUIDs
- **Dependencies**: Nothing external
- **Who calls SURI (directly)**:
  - Nagios
  - ETDs
  - Hydrus
  - Dor-Services-App
  - Argo

![overview diagram](https://docs.google.com/drawings/d/e/2PACX-1vQGCQGaWbFRRVGBck2K6RoJgGaol4s0-_EShvMSQcIWo80rSEGdBCixpLw3MOoUj9tvVd-73-GbKJlS/pub?w=2544&h=1302)
[Link to diagram in Google Drawings](https://docs.google.com/drawings/d/1_lBxiJMgB4Q71JKHytL4FlP8SoDKkEg1S8Wi9pb5V-A/edit?usp=sharing)

## SURI Calls

URI                                        | POST                  | GET                                | PUT (new)                           | PUT (existing)              | DELETE
------------------------------------------ | --------------------- | ---------------------------------- | ----------------------------------- | --------------------------- | ------
`/namespaces`                              | create new profile    | all namespaces                     | n/a                                 | n/a                         | n/a
`/namespaces/{namespace}`                  | n/a                   | namespace xml                      | create new profile                  | replace current profile     | delete profile & identifiers
`/namespaces/{namespace}/template`         | n/a                   | current template                   | add template to profile             | replace template in profile | delete template
`/namespaces/{namespace}/privileges`       | n/a                   | all privilege data                 | add privilege data if none is there | replace privilege data      | delete all privilege data
`/namespaces/{namespace}/agent/{agent_id}` | n/a                   | privilege data for specified agent | add privileges data if not present  | replace privilege data      | delete specified privilege data
`/namespaces/{namespace}/identifiers`      | Mint a new identifier | get all identifiers                | n/a                                 | n/a                         | delete all identifiers
`/namespaces/{namespace}/identifiers/{id}` | n/a                   | identifier value                   | assert new identifier               | 400 error                   | delete specific identifier

1. POST `/namespaces`
  - **Input**: namespace profile XML (minimum is name only)
  - **Output response**: 201 Created
  - **header location**: URI of created namespace
  - **content**: URI of created namespace
2. PUT `/namespaces/{namespace}`
  - **Input:** content optional
  - **Output response**: 201 Created (if created); 200 OK (if replaced)
  - **header location**: URI of created namespace
  - **content**: URI of created namespace
3. GET `/namespaces/{namespace}`
  - **Output response:** 200 OK
  - **content:** namespace profile XML (default representation)
4. DELETE `/namespaces/{namespace}`
  - **Output**: 204 No Content
5. PUT `/namespaces/{namespace}/template`
  - **Input:** content type: text/plain; new template value
  - **Output:** 201 Created (if created); 200 OK (if replaced)
  - **header location:** URI of created namespace
  - **content:** URI of created namespace
6. PUT `/namespaces/{namespace}/agent/{agent_id}`
  - **Input:** content type: application/xml; XML snippet
  - **Output:** 201 Created (if created); 200 OK (if replaced)
  - **header location:** URI of created namespace
  - **content:** URI of created namespace
7. DELETE  /namespaces/{namespace} | /namespaces/{namespace}/template | /namespaces/{namespace}/agent/{agent_id}
  - **Output:** 204 No Content
8. POST `/namespaces/{namespace}/identifiers[?quantity=n,response=xml|text]`
  - **Input:** no content (generated); value (asserted).  The quantity parm causes "n" identifiers to be minted (meaningless when asserting identifiers)
  - **Output:** new identifier value(s); default style is plain text, but either text or XML return format can be requested
9. PUT `/namespaces/{namespace}/identifiers/{identifier}`
  - **Input:** no content
  - **Output:** no content
10. GET `/namespaces/{namespace}/identifiers/{identifier}`
  - **Output:** identifier xml (default representation)
11. GET `/namespaces/{namespace}/identifiers`
  - **Output:** all identifier values, xml (default representation)

## SURI Endpoints Testing

- Last Tested: 2017-07-19
- User(s): `labware` (mint IDs only) & `dor` (full admin privileges)

### SURI-Test

URI                                        | POST                                | GET | PUT (new)          | PUT (existing)   | DELETE
------------------------------------------ | ----------------------------------- | --- | ------------------ | ---------------- | ------
`/namespaces`                              | NOT TESTED                          | OK  | N/A                | N/A              | N/A
`/namespaces/{namespace}`                  | N/A                                 | OK  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/template`         | N/A                                 | OK  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/privileges`       | N/A                                 | OK  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/agent/{agent_id}` | N/A                                 | OK  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/identifiers`      | WRONG RESPONSE (409), Right content | OK  | N/A                | N/A              | NOT TESTED
`/namespaces/{namespace}/identifiers/{id}` | N/A                                 | OK  | OK, 204 best here? | OK (400 / Error) | NOT TESTED

1. GET `/namespaces`
    - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces`
    - **Output Header:**
      ```
      HTTP/1.1 200 OK
      Date: Wed, 19 Jul 2017 18:18:07 GMT
      Content-Type: application/xml
      ```
    - **Output Content:**
      ```xml
      <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
      <namespaces>
        <namespace>
          <name>testing</name>
          <template>r:zznnnzznn</template>
          <agent id="suritest">
            <permission>mint</permission>
            <permission>delete</permission>
            <permission>admin</permission>
          </agent>
          <created>2008-12-8.15.26. 51. 357200000</created>
          <createdBy>suritest</createdBy>
          <updated>2008-12-8.15.26. 51. 357200000</updated>
          <updatedBy>suritest</updatedBy>
        </namespace>
        <namespace>
          <name>druid</name>
          <template>r:zznnnzznnnn</template>
          <agent id="dor">
            <permission>mint</permission>
            <permission>delete</permission>
            <permission>admin</permission>
          </agent>
          <agent id="labware">
            <permission>mint</permission>
          </agent>
          <agent id="salt">
            <permission>mint</permission>
          </agent>
          <agent id="xforms">
            <permission>mint</permission>
          </agent>
          <agent id="hydra-etd">
            <permission>mint</permission>
          </agent>
          <created>2009-8-6.13.3. 0. 606204000</created>
          <createdBy>dor</createdBy>
          <updated>2011-5-5.16.9. 54. 548281000</updated>
          <updatedBy>dor</updatedBy>
        </namespace>
      </namespaces>
      ```
2. GET `/namespaces/{namespace}`
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid`
  - **Output response:**
    ```
    HTTP/1.1 200 OK
    Date: Wed, 19 Jul 2017 18:28:48 GMT
    Content-Type: application/xml
    ```
  - **Output content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <namespace>
      <name>druid</name>
      <template>r:zznnnzznnnn</template>
      <agent id="dor">
        <permission>mint</permission>
        <permission>delete</permission>
        <permission>admin</permission>
      </agent>
      <agent id="labware">
        <permission>mint</permission>
      </agent>
      <agent id="salt">
        <permission>mint</permission>
      </agent>
      <agent id="xforms">
        <permission>mint</permission>
      </agent>
      <agent id="hydra-etd">
        <permission>mint</permission>
      </agent>
      <created>2009-8-6.13.3. 0. 606204000</created>
      <createdBy>dor</createdBy>
      <updated>2011-5-5.16.9. 54. 548281000</updated>
      <updatedBy>dor</updatedBy>
    </namespace>
    ```
3. GET `/namespaces/{namespace}/template`
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/template`
  - **Output response:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 18:34:59 GMT
    Location: https://sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/template/r:zznnnzznnnn
    Content-Type: text/plain
    ```
  - **Output content:**
    ```
    r:zznnnzznnnn
    ```
4. GET `/namespaces/{namespace}/privileges`
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/privileges`
  - **Output response:**
    ```
    HTTP/1.1 200 OK
    Date: Wed, 19 Jul 2017 18:37:59 GMT
    Content-Type: application/xml
    ```
  - **Output content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <agents>
      <agent id="dor">
        <permission>mint</permission>
        <permission>delete</permission>
        <permission>admin</permission>
      </agent>
      <agent id="labware">
        <permission>mint</permission>
      </agent>
      <agent id="salt">
        <permission>mint</permission>
      </agent>
      <agent id="xforms">
        <permission>mint</permission>
      </agent>
      <agent id="hydra-etd">
        <permission>mint</permission>
      </agent>
    </agents>
    ```
6. GET `/namespaces/{namespace}/agent/{agent_id}`
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/agent/labware`
  - **Output header:**
    ```
    HTTP/1.1 200 OK
    Date: Wed, 19 Jul 2017 18:40:34 GMT
    Content-Type: application/xml
    ```
  - **Output content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <agent id="labware">
      <permission>mint</permission>
    </agent>
    ```
8. POST `/namespaces/{namespace}/identifiers[?quantity=n,response=xml|text]`
  - **Input:** `curl -X POST https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers`
    - **Output header:**
      ```
      HTTP/1.1 201 Created
      Date: Wed, 19 Jul 2017 18:48:55 GMT
      Location: https://sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/bh643ng3191
      Content-Type: text/plain
      Transfer-Encoding: chunked
      ```
    - **Output content:** `fv478bj4022`
  - **Input:** `curl -X POST 'https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers?quantity=2'`
    - **Output header:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 18:50:13 GMT
    Location: https://sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/
    Content-Type: text/plain
    Transfer-Encoding: chunked
    ```
    - **Output content:**
    ```
    gb640dy2493
    db999tq8699
    ```
  - **Input:** `curl -X POST 'https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers?quantity=2&response=xml'`
    - **Output header:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 18:51:37 GMT
    Location: https://sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/hr312pz3289
    Content-Type: application/xml
    Content-Length: 206
    ```
    - **Output content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <identifiers>
      <identifier>
        <created>2017-7-19.11.50. 54. 854188000</created>
        <createdBy>labware</createdBy>
        <id>hn026jz3972</id>
      </identifier>
    </identifiers>
    ```
3. GET `/namespaces/{namespace}/identifiers` (using dor, labware doesn't work for this call)
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers`
  - **Output response:**
  ```
  HTTP/1.1 409 Conflict
  Date: Wed, 19 Jul 2017 19:01:22 GMT
  Content-Type: text/html;charset=utf-8
  Content-Length: 1004
  ```
  - **Output content:**
  ```XML
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <identifiers>
    <identifier>
      <created>2009-8-6.13.3. 59. 147454000</created>
      <createdBy>salt</createdBy>
      <id>hy245ps4154</id>
    </identifier>
    <identifier>
      <created>2009-8-6.13.48. 11. 835552000</created>
      <createdBy>salt</createdBy>
      <id>sd300hq1927</id>
    </identifier>
    <identifier>
      <created>2009-8-7.9.22. 25. 608127000</created>
      <createdBy>salt</createdBy>
      <id>rv064hf1832</id>
    </identifier>
    ...
  ```
10. GET `/namespaces/{namespace}/identifiers/{identifier}`
  - **Input:** `curl https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/gb640dy2493`
  - **Output header**:
  ```
  HTTP/1.1 200 OK
  Date: Wed, 19 Jul 2017 19:04:11 GMT
  Content-Type: application/xml
  ```
  - **Output content**:
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <identifier>
    <created>2017-7-19.11.49. 30. 411105000</created>
    <createdBy>labware</createdBy>
    <id>gb640dy2493</id>
  </identifier>
  ```
9. PUT `/namespaces/{namespace}/identifiers/{identifier}`
  - **Input:** `curl -X PUT https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/gb640dy2494`
  - **Output response:**
  ```
  HTTP/1.1 204 No Content
  Date: Wed, 19 Jul 2017 19:23:53 GMT
  Pragma: No-cache
  Cache-Control: no-cache
  Expires: Wed, 31 Dec 1969 16:00:00 PST
  Content-Length: 0
  Content-Type: text/plain
  ```
  - **Output content:** no content
9. PUT `/namespaces/{namespace}/identifiers/{identifier that exists}`
  - **Input:** `curl -X PUT https://username:password@sul-lyberservices-test.stanford.edu/suri2/namespaces/druid/identifiers/gb640dy2494`
  - **Output response:**
  ```
  HTTP/1.1 400 Bad Request
  Date: Wed, 19 Jul 2017 19:25:54 GMT
  Pragma: No-cache
  Cache-Control: no-cache
  Expires: Wed, 31 Dec 1969 16:00:00 PST
  Content-Type: text/plain
  Connection: close
  Transfer-Encoding: chunked
  ```
  - **Output content:**
  ```
  ID already in use
  ```

### SURI-Dev

URI                                        | POST                                | GET                 | PUT (new)          | PUT (existing)   | DELETE
------------------------------------------ | ----------------------------------- | ------------------- | ------------------ | ---------------- | ------
`/namespaces`                              | NOT TESTED                          | OK                  | N/A                | N/A              | N/A
`/namespaces/{namespace}`                  | N/A                                 | OK                  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/template`         | N/A                                 | OK                  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/privileges`       | N/A                                 | OK               | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/agent/{agent_id}` | N/A                                 | OK  | NOT TESTED         | NOT TESTED       | NOT TESTED
`/namespaces/{namespace}/identifiers`      | WRONG RESPONSE (409), Content times out | OK  | N/A                | N/A              | NOT TESTED
`/namespaces/{namespace}/identifiers/{id}` | N/A                                 | OK  | OK, 204 best here? | OK (400 / Error) | NOT TESTED

1. GET `/namespaces`
    - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces`
    - **Output Header:**
    ```
    HTTP/1.1 200 OK
    Date: Wed, 19 Jul 2017 19:29:39 GMT
    Content-Type: application/xml
    ```
    - **Output Content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <namespaces>
      <namespace>
        <name>rd</name>
        <template>r:zznnnzznnn</template>
        <agent id="suritest">
          <permission>admin</permission>
          <permission>mint</permission>
        </agent>
        <created>2008-7-25.16.37. 40. 688819000</created>
        <createdBy>suritest</createdBy>
        <updated>2008-7-25.16.52. 45. 860178000</updated>
        <updatedBy>suritest</updatedBy>
      </namespace>
      <namespace>
        <name>oai:library.stanford.edu:aquImmigrationCommission</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-8-16.22.34. 46. 413612000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-16.22.34. 46. 413612000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>oai:sulair.stanford.edu</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>delete</permission>
          <permission>admin</permission>
          <permission>mint</permission>
        </agent>
        <created>2008-8-15.13.37. 55. 842079000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-15.13.37. 55. 842079000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>dr</name>
        <template>r:zznnnzznnnn</template>
        <agent id="dor">
          <permission>mint</permission>
          <permission>admin</permission>
          <permission>delete</permission>
        </agent>
        <agent id="suritest">
          <permission>admin</permission>
          <permission>mint</permission>
        </agent>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-9-8.10.27. 17. 723953000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-9-8.10.27. 17. 723953000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>testSpace</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-8-15.23.20. 32. 987725000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-15.23.20. 32. 987725000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>oai:library.stanford.edu/aquImmigrationCommission</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-8-16.19.50. 39. 86784000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-16.19.50. 39. 86784000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>oai:library.stanford.edu/aquMenuez</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-8-16.19.51. 46. 435009000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-16.19.51. 46. 435009000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>oai:library.stanford.edu:aquMenuez</name>
        <template>r:zznnnzznn</template>
        <agent id="xforms">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <created>2008-8-16.19.56. 34. 704762000</created>
        <createdBy>xforms</createdBy>
        <updated>2008-8-16.19.56. 34. 704762000</updated>
        <updatedBy>xforms</updatedBy>
      </namespace>
      <namespace>
        <name>druid</name>
        <template>r:zznnnzznnnn</template>
        <agent id="dor">
          <permission>mint</permission>
          <permission>delete</permission>
          <permission>admin</permission>
        </agent>
        <agent id="labware">
          <permission>mint</permission>
        </agent>
        <agent id="xforms"><permission>mint</permission>
      </agent>
      <agent id="hydra-etd">
        <permission>mint</permission>
      </agent>
      <created>2009-8-31.14.4. 31. 274235000</created>
      <createdBy>dor</createdBy>
      <updated>2011-5-5.16.8. 45. 721638000</updated>
      <updatedBy>dor</updatedBy>
    </namespace>
    </namespaces>
    ```
2. GET `/namespaces/{namespace}`
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid`
  - **Output response:**
  ```
  HTTP/1.1 200 OK
  Date: Wed, 19 Jul 2017 19:34:37 GMT
  Content-Type: application/xml
  ```
  - **Output content:**
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <namespace>
    <name>druid</name>
    <template>r:zznnnzznnnn</template>
    <agent id="dor">
      <permission>mint</permission>
      <permission>delete</permission>
      <permission>admin</permission>
    </agent>
    <agent id="labware">
      <permission>mint</permission>
    </agent>
    <agent id="xforms">
      <permission>mint</permission>
    </agent>
    <agent id="hydra-etd">
      <permission>mint</permission>
    </agent>
    <created>2009-8-31.14.4. 31. 274235000</created>
    <createdBy>dor</createdBy>
    <updated>2011-5-5.16.8. 45. 721638000</updated>
    <updatedBy>dor</updatedBy>
   </namespace>
   ```
3. GET `/namespaces/{namespace}/template`
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/template`
  - **Output response:**
  ```
  HTTP/1.1 201 Created
  Date: Wed, 19 Jul 2017 19:35:53 GMT
  Location: https://sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/template/r:zznnnzznnnn
  Content-Type: text/plain
  ```
  - **Output content:**
  ```
  r:zznnnzznnnn
  ```
4. GET `/namespaces/{namespace}/privileges`
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/privileges`
  - **Output response:**
  ```
  HTTP/1.1 200 OK
  Date: Wed, 19 Jul 2017 19:39:43 GMT
  Content-Type: application/xml
  ```
  - **Output content:**
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <agents>
    <agent id="dor">
      <permission>mint</permission>
      <permission>delete</permission>
      <permission>admin</permission>
    </agent>
    <agent id="labware">
      <permission>mint</permission>
    </agent>
    <agent id="xforms">
      <permission>mint</permission>
    </agent>
    <agent id="hydra-etd">
      <permission>mint</permission>
    </agent>
  </agents>
  ```
6. GET `/namespaces/{namespace}/agent/{agent_id}`
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/agent/labware`
  - **Output header:**
  ```
  HTTP/1.1 200 OK
  Date: Wed, 19 Jul 2017 19:40:54 GMT
  Content-Type: application/xml
  ```
  - **Output content:**
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <agent id="labware">
    <permission>mint</permission>
  </agent>
  ```
8. POST `/namespaces/{namespace}/identifiers[?quantity=n,response=xml|text]`
  - **Input:** `curl -X POST https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers`
    - **Output header:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 19:42:16 GMT
    Location: https://sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/ff698fw6178
    Content-Type: text/plain
    Transfer-Encoding: chunked
    ```
    - **Output content:** `ff698fw6178`
  - **Input:** `curl -X POST 'https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers?quantity=2'`
    - **Output header:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 19:43:00 GMT
    Location: https://sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/
    Content-Type: text/plain
    Transfer-Encoding: chunked
    ```
    - **Output content:**
    ```
    ng368js2839
    yx240wy1243
    ```
  - **Input:** `curl -X POST 'https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers?quantity=2&response=xml'`
    - **Output header:**
    ```
    HTTP/1.1 201 Created
    Date: Wed, 19 Jul 2017 19:43:21 GMT
    Location: https://sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/
    Content-Type: application/xml
    Content-Length: 330
    ```
    - **Output content:**
    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <identifiers>
      <identifier>
        <created>2017-7-19.12.43. 21. 876134000</created>
        <createdBy>labware</createdBy>
        <id>br121wq6889</id>
      </identifier>
      <identifier>
        <created>2017-7-19.12.43. 21. 923734000</created>
        <createdBy>labware</createdBy>
        <id>xx386fb1202</id>
      </identifier>
    </identifiers>
    ```
9. GET `/namespaces/{namespace}/identifiers` (using dor, labware doesn't work for this call)
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers`
  - **Output response:**
  ```
  HTTP/1.1 409 Conflict
  Date: Wed, 19 Jul 2017 19:44:22 GMT
  Content-Type: text/html;charset=utf-8
  Content-Length: 1004
  ```
  - **Output content:** Times out
10. GET `/namespaces/{namespace}/identifiers/{identifier}`
  - **Input:** `curl https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/br121wq6889`
  - **Output header**:
  ```
  HTTP/1.1 200 OK
  Date: Wed, 19 Jul 2017 19:47:36 GMT
  Pragma: No-cache
  Cache-Control: no-cache
  Expires: Wed, 31 Dec 1969 16:00:00 PST
  Content-Type: application/xml
  Content-Length: 179
  ```
  - **Output content**:
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <identifier>
    <created>2017-7-19.12.43. 21. 876134000</created>
    <createdBy>labware</createdBy>
    <id>br121wq6889</id>
  </identifier>
  ```
9. PUT `/namespaces/{namespace}/identifiers/{identifier}`
  - **Input:** `curl -X PUT https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/br121wq6890`
  - **Output response:**
  ```
  HTTP/1.1 204 No Content
  Date: Wed, 19 Jul 2017 19:48:41 GMT
  Pragma: No-cache
  Cache-Control: no-cache
  Expires: Wed, 31 Dec 1969 16:00:00 PST
  Content-Length: 0
  Content-Type: text/plain
  ```
  - **Output content:** no content
9. PUT `/namespaces/{namespace}/identifiers/{identifier that exists}`
  - **Input:** `curl -X PUT https://username:password@sul-lyberservices-dev.stanford.edu/suri2/namespaces/druid/identifiers/br121wq6890`
  - **Output response:**
  ```
  HTTP/1.1 400 Bad Request
  Date: Wed, 19 Jul 2017 19:49:14 GMT
  Pragma: No-cache
  Cache-Control: no-cache
  Expires: Wed, 31 Dec 1969 16:00:00 PST
  Content-Type: text/plain
  Connection: close
  Transfer-Encoding: chunked
  ```
  - **Output content:**
  ```
  ID already in use
  ```
