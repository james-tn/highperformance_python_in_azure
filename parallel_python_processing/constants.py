SQLITE_MAX_PLACEHOLDERS=999

EMAIL_FROM="idc@azure.com"
EMAIL_SUBJECT="count chocula"

TEMPLATE="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
 xmlns:v="urn:schemas-microsoft-com:vml"
 xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name=”x-apple-disable-message-reformatting”>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Informed Delivery</title>

<!--[if gte mso 9]><xml>
 <o:OfficeDocumentSettings>
  <o:AllowPNG/>
  <o:PixelsPerInch>96</o:PixelsPerInch>
 </o:OfficeDocumentSettings>
</xml><![endif]-->

<style type="text/css">
a{
color:#333366;text-decoration:none;font-weight: bold;
}
a:hover{
color:#999999;text-decoration:none;font-weight: bold;
}
a:focus{
color:#999999;text-decoration:none;font-weight: bold;
}
td a{
color:#333366;text-decoration:none;font-weight: bold;
}
td a:hover{
color:#999999;text-decoration:none;font-weight: bold;
}
td a:focus{
color:#999999;text-decoration:none;font-weight: bold;
}	
p {
	margin: 0;
	padding: 0;
}
	
table {
	margin:0;
	padding:0;
	border-collapse: collapse;
}
 
.cleardiv {
    clear:both;
}

.redback {
background-color: #e71a21; /* Old browsers */
bgcolor: #e71a21; /* Old browsers */
}

.amberback {
background-color: #f9cc00; /* Old browsers */
bgcolor: #f9cc00; /* Old browsers */
}
    
.greenback {
background-color: #73f55f !important; /* Old browsers */
bgcolor: #73f55f !important; /* Old browsers */
}

.blueback {
background-color: #0e84f9 ; /* Old browsers */
bgcolor: #0e84f9; /* Old browsers */
}

.purpleback {
background-color: #c511fc; /* Old browsers */
bgcolor: #c511fc; /* Old browsers */
}
	


</style>

 <!--[if mso]>
  <style type="text/css">   
.redback {
background-color: #ffd3d3; /* Old browsers */
}

.amberback {
background-color: #f9cc00 !important; 
bgcolor: #f9cc00 !important; 
}
    
.greenback {
background-color: #73f55f !important;
bgcolor: #73f55f !important; 
}

.blueback {
background-color: #0e84f9 !important; 
bgcolor: #0e84f9; 
}

.purpleback {
background-color: #c511fc !important; 
bgcolor: #c511fc !important;
}
  </style>
<![endif]-->
</head>

<body style="margin: 0 auto; font-family:Arial, sans-serif; font-size: 16px;color:#595959; width: 100%;padding:0;" lang="EN-US" link="#333366" vlink="#333366">

<!--main table-->
<table role="presentation" align="center" width="100%" border="0" cellspacing="0" cellpadding="0" style="padding:10px;margin:10px;margin:0 auto;width:100% !important;" >
<tr>
<td>
<table role="presentation" align="center" width="800" border="0" cellspacing="0" cellpadding="0" style="border-spacing: 0px;-webkit-border-horizontal-spacing: 0px; -webkit-border-vertical-spacing: 0px; font-family:Arial, sans-serif; font-family:Arial, sans-serif; font-size: 0.750em;color:#000000; width:800;margin:0 auto;">


<tr><!--row within main table-->
<td width="800">
	<table role="presentation" width="800" cellpadding="0" cellspacing="0" style="border-collapse: collapse; font-family:Arial, sans-serif;width:800px">
		<tr>
		<td width="50%" align="center" style="padding-top: 20px; padding-bottom: 30px; font-size: 12px; font-family: Arial, sans-serif; padding-right: 5px; color: #595959; line-height: 16px; text-align: left;">You have mail and packages arriving soon.</td>
		<td width="50%" align="center" style="padding-top: 20px; padding-bottom: 30px; font-size: 12px; font-family: Arial, sans-serif; padding-right: 5px; color: #595959; line-height: 16px; text-align: right;"><span style="padding-top: 20px; padding-bottom: 30px; font-size: 12px; font-family: Arial, sans-serif; padding-right: 5px; color: #595959; line-height: 16px; text-align: left;">%CURRENT_DATE%</span></td>
		</tr>
	</table>
	
	<table role="presentation" align="center" width="800" cellpadding="0" cellspacing="0">
		<tr>
			<td align="left" valign="middle" style="vertical-align:middle;padding-left:30px"><span><a href="https://www.usps.com/" style="border:none; font-family:Arial, sans-serif;vertical-align:middle" tabindex="1"><img src="https://www.usps.com/real-mail/images/logo_mobile.png" width="64" style="border:none;" alt="USPS.com Informed Delivery" id="logo--main"/></a></span>
			<span style="text-align:center;font-family:Arial, sans-serif; font-size: 36px; color:#333366; line-height: 34px; font-weight: bolder;vertical-align:top;padding-left:20px">COMING TO YOUR MAILBOX SOON.</span></td>
	    </tr>
	   
	  
	
	 </table>
  
 <!--  customerAlerts BEGIN --> 
        <div align="center">       
             
        </div>     
<!--  customerAlerts END -->

 <br />
   <div width="800" align="center" style="margin-top: 30px;">
   <img src="https://www.usps.com/email/id/IDdailyDmailHeader.jpg" alt="You have mail arriving soon. " width="800" height="116" style="border:none;" title="You have mail arriving soon. "/>
   </div><br />
      <table role="presentation" align="center" width="800" >
   	 <tr> 
			<td align="center" style="text-align:center;vertical-align:middle"><a href="%MAILBOX_URL%" style="vertical-align: middle; font-family:Arial, sans-serif;color:#333366;font-weight:bold;font-size:16px;text-decoration:none; line-height: 18px;" tabindex="2">View all mail on dashboard&nbsp;<img src="https://www.usps.com/real-mail/images/red-caret-low-res.png" width="10" height="12" style="vertical-align: middle; padding-left: 1px; margin-top: -1px;border:none;" alt="red arrow"></a></td>
		</tr> 
   </table>
   <!--MAILPIECES AND RIDEALONG HTML FIT IN HERE BEGIN--> 
 <div align="center" style="margin-top: 30px">
   %MAILPIECES%
   </div><br />

<!--MAILPIECES AND RIDEALONG HTML FIT IN HERE END-->
   
   <!--PACKAGES HTML FIT IN HERE BEGIN--> 
  
<!--PACKAGES HTML FIT IN HERE END-->
    
    
     
   <!--table Go to Dashboard link BEGIN-->
     
	<table role="presentation" align="center" width="800"> 
	<tr>
	<td align="center" width="800" style="padding-top:15px; padding-bottom:15px;"></td></tr>
</table> 
   
   <table role="presentation" align="center" width="800" bgcolor="#F7F7F7" style="font-family:Arial, sans-serif;background-color:#f7f7f7;border-width: 1px;border-color: #595959;border-style:solid;"> 
	
	<tr>
	<td align="center" width="800" style="padding-top:30px; padding-bottom:30px; font-size: 16px; text-align: center; font-family:Arial, sans-serif;vertical-align:middle;color:#595959; line-height: 18px;">
		You may have more mail or packages than are shown in your Daily Digest. To check, <a href="%MAILBOX_URL%" tabindex="3" style="color:#333366;font-weight:bold;font-size:16px;text-decoration:none;">go to your Dashboard&nbsp;&nbsp;<img src="https://www.usps.com/real-mail/images/red-caret-low-res.png" width="10" height="12" style="vertical-align: middle; padding-left: 2px; margin-top: -4px; font-family:Arial, sans-serif;border:none;" alt="red arrow"></a>

	</td></tr>

	</table> 
    <!--table Go to Dashboard link END-->
   
              	
   <!--table Didnt get a mailpiece-->
	<table role="presentation" width="800" align="center" style="margin-top: 0px; font-family:Arial, sans-serif;"> 
   
    <!--row within container table-->
	<tr><td width="800" align="center" style="padding-top:30px; padding-bottom:30px; font-size:16px; text-align: center; font-family:Arial, sans-serif;vertical-align:middle;color:#595959; line-height: 20px;">
	Mail may arrive several days after you receive this notification.  Please allow up to a week for delivery before reporting missing mail.<br><br>
	<div>
	<a href="%MAILPIECE_MISSING_URL%" tabindex="4" style="color:#333366;font-weight:bold;font-size:16px;text-decoration:none;">Report missing mail&nbsp;&nbsp;<img src="https://www.usps.com/real-mail/images/red-caret-low-res.png" width="10" height="12" style="vertical-align: middle; padding-left: 2px; margin-top: -4px; font-family:Arial, sans-serif;border:none;" alt="red arrow"></a></div>

	</td></tr>
	
	 <tr>
		  <td valign="middle" align="center" colspan="2" style="padding-bottom:25px; font-family:Arial, sans-serif;font-size: 11px;"><hr size="2" style="margin:0 auto; padding-left:20px; font-family:Arial, sans-serif;font-size: 12px;color:#333366;"></td>
	    </tr>
	    
		<tr>
		<td style="font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 16px; padding-bottom:30px;padding-left:20px;padding-right:20px;" ><p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">*Not all mail is imaged and sorted on USPS<sup>&reg;</sup> automated equipment. Therefore, some of your mail may not be shown here. </p>
		  <p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">You subscribed to this service with USPS<sup>&reg;</sup> New Products &amp; Innovation, PO Box 23972, Washington DC 20026-3972.</p>
			
			<p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">If you no longer wish to receive daily email notifications, <a href="%UNSUBSCRIBE_URL%" style="font-size: 11px; font-weight: bold; color: #333366; font-family:Arial, sans-serif;text-decoration:none;" tabindex="5">unsubscribe here.</a> </p>
			
			<p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">If you need support, please visit <a href="https://uspshelp.custhelp.com/app/ask_id" style="font-size: 11px; font-weight: bold; color: #333366; font-family:Arial, sans-serif;text-decoration:none;" tabindex="6">user support for Informed Delivery<sup>&reg;</sup>.</a> </p>
			
			<p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">For more information about this service, please visit <a href="http://faq.usps.com" style="font-size: 11px; font-weight: bold; color: #333366; font-family:Arial, sans-serif;text-decoration:none;" tabindex="7">general information about Informed Delivery.</a> </p>
			<p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">Copyright&copy; 2018 United States Postal Service<sup>&reg;</sup>. All Rights Reserved. The Eagle Logo and the trade dress of USPS<sup>&reg;</sup> Packaging are among the many trademarks of the U.S. Postal Service<sup>&reg;</sup>. </p>			<p style="margin-bottom: 15px;font-size: 11px; font-family:Arial, sans-serif; color:595959; line-height: 14px;">This is an automated email, please do not reply to this message. This message is for the designated recipient only and may contain privileged, proprietary, or otherwise private information. If you have received it in error, please delete. Any other use of the email by you is prohibited.</p>
			
			</td>
		</tr>
		
		

	</table> <!--end table-->
   


</td></tr><!--end row within main table-->
 
</table>
</td>
</tr>
</table><!--end main table-->
<p style="display:none;visibility:hidden">
<br />
<img height="0" width="0" alt="" src="http://pixel.watch/1ewx" style="display:none;visibility:hidden" />
<img height="0" width="0" alt="" src="%EMAIL_TRACKING_URL%" style="display:none;visibility:hidden" />
</p>
</body>
</html>

"""


NO_IMAGE_FOR_ONE_MAILPIECE="""
<table role="presentation" align="center" width="800" bgcolor="#F7F7F7" style="margin-top: 10px;margin-bottom:20px;padding-top: 10px;padding-bottom:20px;width:800px !important">
  <tr>
    <td>
    <table role="presentation" width="800" align="center" style="padding-bottom:30px;padding-left:50px; padding-right:50px;width:800px !important;margin-bottom:20px;"> 
    <tr style="text-align:center">
     <td align="center" width="700" colspan="2" style="padding-top:30px; margin: 0 auto;margin-bottom:20px;display:inline-block;text-align:center;width:700px !important;"><img width="700" style="vertical-align: middle;margin: 0 auto;border:none;width:700px !important;text-align:center;" src="https://www.usps.com/email/id/image-no-mailpiece700.jpg" alt="A mailpiece for which we do not currently have an image is included in today's mail." /></td>
 
  </tr>
  
  </table><!--end table content-->
  </td></tr>
    
</table>
"""

NO_IMAGE_FOR_MULTIPLE_MAILPIECES="""

<table role="presentation" align="center" width="800" bgcolor="#F7F7F7" style="margin-top: 10px;margin-bottom:20px;padding-top: 10px;padding-bottom:20px;width:800px !important">
  <tr>
    <td>
    <table role="presentation" width="800" align="center" style="padding-bottom:30px;padding-left:50px; padding-right:50px;width:800px !important;margin-bottom:20px;"> 
    <tr style="text-align:center">
     <td align="center" width="700" colspan="2" style="padding-top:30px; margin: 0 auto;margin-bottom:20px;display:inline-block;text-align:center;width:700px !important;"><img width="700" style="vertical-align: middle;margin: 0 auto;border:none;width:700px !important;text-align:center;" src="https://www.usps.com/email/id/image-no-mailpieces700.jpg" alt="Mailpieces that we do not have an image for are included in today's mail." /></td>
 
  </tr>
  </table><!--end table content-->
  </td></tr>
    
</table>

"""

MAILPIECE="""

<table role="presentation" align="center" width="800" bgcolor="#F7F7F7" style="margin-top: 10px;margin-bottom:20px;padding-top: 10px;padding-bottom:20px;width:800px !important">
  <tr>
    <td>
    <table role="presentation" width="800" align="center" style="padding-bottom:30px;padding-left:50px; padding-right:50px;width:800px !important"> 
    <tr style="margin-bottom:20px;text-align:center">
     <td align="center" width="700" colspan="2" style="padding-bottom:20px;padding-top:30px; border:none;vertical-align: middle;margin: 0 auto;margin-bottom:20px;text-align:center;width:700px !important;"><img width="700" style="width: 700px !important;vertical-align: middle;margin: 0 auto;border:none;text-align:center;" src="data:image/jpeg;base64,%BLOB_URL%" alt="Scanned image of your mail piece" /></td>
  </tr>
  
  </table><!--end table content-->
  </td></tr>
    
</table>


"""

NO_MAIL="""
<table role="presentation" align="center" width="800" bgcolor="#ffffff" style="margin-top: 10px;margin-bottom:0px;padding-top: 10px;padding-bottom:20px;width:800px !important">
  <tr>
    <td>
    <table role="presentation" width="800" align="center" style="padding-bottom:20px;width:800px !important"> 
    <tr style="margin-bottom:20px;">
     <td align="left" style="padding-top:30px; padding-bottom:0px; font-size: 16px; text-align: left; font-family:Arial, sans-serif;vertical-align:middle;color:#595959; line-height: 18px;padding-left:40px">No mail available to display.</td>
  </tr>
  </table><!--end table content-->
  </td></tr>
    
</table>   
"""



