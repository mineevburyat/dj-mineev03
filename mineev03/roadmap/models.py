from django.db import models

# Create your models here.
class ResourceStudy(models.Model):
    '''ресурсы для самостоятельного ознакомления с темой (статья, глава книги, 
    таймсет видео и пр.). Ссылка на отличную статью, видео, главу книги более 
    глубоко раскрывающая тему. TODO: продумать систему оценки качества и 
    актуальности статьи'''
    class Meta:
        verbose_name = "ссылка на ресурс по теме"
        verbose_name_plural = 'ссылки на ресурсы'
    name = models.CharField(max_length=30, verbose_name="Название ресурса")
    url = models.URLField(verbose_name="Ссылка на ресурс")
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class ResourceLern(models.Model):
    '''ресурсы для совместного обучания в составе группы, полноценный курс, книга,
    видеоканал. TODO: отлично будет если у курса есть API отражающий уровень 
    прохождения курса. И отображение этого уровня непосредственно в роадмап для зарегистрированного
    пользователя'''
    class Meta:
        verbose_name = "ссылка на курс"
        verbose_name_plural = 'ссылки на курсы'
    name = models.CharField(max_length=30, verbose_name="Название курса")
    url = models.URLField(verbose_name="Ссылка на курс")
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Topik(models.Model):
    '''Тема обсуждения, изучения. основная тема из плана изучения. 
    Отражающая текущий уровень усвоения. Связана с курсами и ресурсами, 
    а так же ключевыми словами'''
    class Meta:
        verbose_name = "тема обсуждения и изучения"
        verbose_name_plural = 'темы обсуждения и изучения'
    name = models.CharField(max_length=35, verbose_name="Краткое название темы")
    name_en = models.CharField(max_length=20, verbose_name='краткое название на английском')
    description = models.TextField(verbose_name="тезисное описание или определение темы")
    current_level = models.SmallIntegerField(verbose_name='Текущий уровень знаний', default=0)
    roadmap = models.ForeignKey(
        'RoadMapStudy', 
        verbose_name='план изучения (roadmap)',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.name_en})"
    
class KeyWord(models.Model):
    '''Ключевые слова для данной темы или ресурса'''
    class Meta:
        verbose_name = "ключевое слово"
        verbose_name_plural = 'ключевые слова'
    word = models.CharField(max_length=35, verbose_name="слово")
    word_en = models.CharField(max_length=20, verbose_name='слово на английском')
    definition = models.TextField(verbose_name="строгое определение")
    
    def __str__(self) -> str:
        return f"{self.word} ({self.word_en})"
    
class RoadMapStudy(models.Model):
    '''Дорожная карта, план, документ, в котором наглядно отображается стратегический план проекта: его главные цели и задачи, сроки исполнения, основные темы.'''
    class Meta:
        verbose_name = "план изучения"
        verbose_name_plural = 'планы изучения'
    name = models.CharField(max_length=35, verbose_name="Название дорожной карты")
    name_en = models.CharField(max_length=20, verbose_name='Название плана изучения на английском')
    description = models.TextField(verbose_name="Краткое описание: цели и задачи, сроки, основные темы")
    
    
    def __str__(self) -> str:
        return f"{self.name} ({self.name_en})"
    
class FaQ(models.Model):
    '''Часто задаваемые вопросы по плану занятий, теме, ключевому слову'''
    class Meta:
        verbose_name = "часто задаваемый вопрос"
        verbose_name_plural = 'часто задаваемые вопросы'
    question = models.CharField(max_length=35, verbose_name="кратко сформированный вопрос")
    answer = models.TextField(verbose_name="Развернутый ответ на вопрос")