# OpenEMR Security Notes - Development Environment
# AI-generated code

## Current Setup
You are running OpenEMR with PHP's built-in development server, which is suitable for 
development and testing but NOT recommended for production use.

## Apache Configuration (for future production deployment)
If you deploy to Apache in production, add these directives to your Apache config:

```apache
<Directory "/Users/nihalmaddala/openemr">
    AllowOverride FileInfo
    Require all granted
</Directory>
<Directory "/Users/nihalmaddala/openemr/sites">
    AllowOverride None
</Directory>
<Directory "/Users/nihalmaddala/openemr/sites/*/documents">
    Require all denied
</Directory>
```

## File Permissions
The documents directory is located at:
/Users/nihalmaddala/openemr/sites/default/documents/

This directory contains sensitive patient information and should be properly secured.

## For Development
The current PHP development server setup is adequate for local development.
Just ensure:
1. The server is only accessible from localhost (127.0.0.1/::1)
2. You don't expose port 8000 to external networks
3. You use proper authentication in OpenEMR

## For Production
When deploying to production, you should:
1. Use a proper web server (Apache, Nginx) with SSL/TLS
2. Apply the Apache/Nginx security configurations
3. Ensure proper file permissions (documents directory should not be web-accessible)
4. Use a firewall to restrict access
5. Keep OpenEMR and all dependencies updated
