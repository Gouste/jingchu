
Git 查看暂存区的文件：
1、查看在暂存区的文件：
git ls-files | grep 文件名
2、删除在暂存区的文件：
git rm --cache 文件名
3、删除存在工作区的文件
git restore --staged 文件名



Git 解决版本冲突的办法:
1、提交git代码时，本地版本与远程仓库版本不一致，导致提交失败  
      需要先进行将远程仓库代码pull一下，注意，pull的时候要使用
【git pull 连接名  分支名 --no-rebase】 or 【git pull 连接名 分支名 --rebase】
 
1.1【git pull 连接名  分支名 --no-rebase】
将代码pull之后，commit tab区域里会展示冲突的版本，然后选择要使用的版本，解决冲突
        后，使用  【git commit -m ""】重新提交，然后使用【git push 连接名 分支名】将代码提
        交到远程仓库                     
   ————这种方法会在本地将你所有的操作留痕，方便查看操作
1.2【git pull 连接名  分支名 --rebase】
将代码pull之后，commit tab区域里会展示冲突的版本，然后选择要使用的版本，解决冲突
        后，使用【git status】查看状态，这时提示你，版本变基中需要使用
【git rebase --continue】结束变基，然后自动进入commit的 vi 界面，填写提交文案后使		
   用wq保存退出，然后使用【git push 连接名 分支名 】重新提交到远程仓库
           ————这种方法提交的代码，不会留选择远程版本还是本地版本的记录，不建议使用
2、什么情况下会出现远程仓库和本地仓库的版本冲突？
2.1、远程仓库的文件与你修改后提交的文件内容不一致。
# 3、注释：
如果只是远程仓库的代码与 你未修改提交的代码不一致引发的版本冲突，那么只需要
【git pull 连接名 分支名】就行了




配置github：
仓库地址：https://github.com/kimpper/UiTest.git
1、登录github
2、打开终端，输入生成秘钥的命令行：
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
或

ssh-keygen -t ed25519 -C "your_email@example.com"
3、点击回车两次，确定文件生成

4、查看当前文件，
      id_xxx 为私钥。
      id_xxx.pub为公钥
把公钥copy到远程仓库

5、在config文件中配置  配置私钥地址 
      HostName[远程仓库的域名地址]
      IdentityFile  ~/.ssh/【私钥文件名】

6、检查代理：ssh-add -l
7、有多余的代理情况下，可以使用  ssh-add -D   删除代理
8、使用命令  ssh-add -K 【私钥路径】 创建新的代理
9、创建成功后，使用  ssh -T 【远程仓库地址】测试连接
10、提示  Hi，shabi... 时，表示连接成功，可以使用


多仓库时，需要创建多秘钥与私钥。创键多个私钥时，需要使用 【秘钥生成命令 -f 路径/文件名】。来生成防止覆盖或生成后重名
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f  路径/文件名
使用则需重复以上步骤进行配置





下载Python：
1、下载Python版本
2、在终端输入Python3查看下载路径
3、进入路径，打开.bash_profile文件，输入：
# Setting PATH for Python 3.8# The original version is saved in 
.bash_profile.pysavePATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PAT
H}"export PATHalias
 python="/Library/Frameworks/Python.framework/Versions/3.8/bin/python3"




连接数据库：
测试环境地址（主机）：test-dgroup.cqx0bweaving.ap-northeast-1.rds.amazonaws.com
 
端口号：3306
 
用户名：dgroup
 
密码：Do4best2018
