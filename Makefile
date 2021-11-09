recreate-migration:
	# find all migration files except those in oscar: we need to preserve default oscar migrations file orders
	find . -path "*/migrations/*.py" ! -path "*/sites/*.py" ! -name "__init__.py" -delete
	pyclean -v .

prune:
	git checkout develop && git pull origin develop && git fetch -p && git branch --merged | egrep -v "(^\*|master|develop)" | xargs git branch -d

ecr-login:
	aws ecr get-login-password --profile $$AWS_PROFILE --region ap-northeast-2 | docker login --username AWS --password-stdin \
    $$(aws sts get-caller-identity --query Account --output text).dkr.ecr.ap-northeast-2.amazonaws.com
