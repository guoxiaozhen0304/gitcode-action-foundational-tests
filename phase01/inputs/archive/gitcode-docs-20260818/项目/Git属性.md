
`.gitattributes` 用于配置 Git 项目中的文件属性，以便更好地控制文件的处理和展示方式。

`.gitattributes` 文件允许你定义文件的属性，例如文件编码、行尾格式、合并策略等，以确保它们在版本控制和协作过程中得到正确处理，可以支持：

- **文件编码**：定义文件的编码，以确保它们在不同的操作系统和编辑器中正确解释
- **行尾格式**：指定文件的行尾格式，如 Unix（LF）、Windows（CRLF）或 Mac（CR）
- **合并策略**：配置文件合并时使用的策略，以避免冲突并确保合并正确进行
- **二进制文件处理**：定义二进制文件的处理方式，以便它们不会被误解为文本文件

### 创建 .gitattributes 文件

1. **登录 GitCode**：首先，请确保你已登录到 GitCode 帐户
2. **进入项目**：进入包含你想要创建 .gitattributes 文件的项目页面
3. **点击添加文件**：在项目页面左上角，点击“添加文件”按钮
4. **命名 .gitattributes 文件**：在文件名字段中，输入 ".gitattributes"（请确保文件名以点号开头）
6. **定义文件属性**：在文件中，定义文件属性和规则。例如，你可以设置文件的编码、行尾格式和合并策略
7. **点击 "Commit new file"**：在页面底部，点击 "Commit new file" 按钮以保存 .gitattributes 文件

### 示例

以下是一个 `Java` 代码文件的示例：

```bash
# Java sources
*.java          text diff=java
*.kt            text diff=kotlin
*.groovy        text diff=java
*.scala         text diff=java
*.gradle        text diff=java
*.gradle.kts    text diff=kotlin

# These files are text and should be normalized (Convert crlf => lf)
*.css           text diff=css
*.scss          text diff=css
*.sass          text
*.df            text
*.htm           text diff=html
*.html          text diff=html
*.js            text
*.jsp           text
*.jspf          text
*.jspx          text
*.properties    text
*.tld           text
*.tag           text
*.tagx          text
*.xml           text

# These files are binary and should be left untouched
# (binary is a macro for -text -diff)
*.class         binary
*.dll           binary
*.ear           binary
*.jar           binary
*.so            binary
*.war           binary
*.jks           binary

# Common build-tool wrapper scripts ('.cmd' versions are handled by 'Common.gitattributes')
mvnw            text eol=lf
gradlew         text eol=lf
```

更多示例可参考 <https://github.com/alexkaratarakis/gitattributes>