# captcha
通过集成开源项目amazoncaptcha，实现的亚马逊验证码解析服务，部署较复杂，建议直接使用docker镜像运行。
 docker run -it --network spider-network -p 8000:8000 -d --name="captcha" 15392680446/dy:captcha  
 /captcha/link 直接传入验证码图片链接进行解析 get请求，有反爬风险
 
 /captcha/image 上传图片文件进行解析 post请求，建议使用此接口
 
 通过模拟浏览器解析验证码，此功能未实现。
 
 
 
 
 服务启动成功测试方法：  
 
GET http://127.0.0.1:8000/
Accept: application/json
