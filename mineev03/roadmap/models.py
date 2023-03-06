from django.db import models

class RoadMapStudy(models.Model):
    '''Дорожная карта обучения: план занятий, в котором наглядно отображается стратегический план проекта: его главные цели и задачи, сроки исполнения, основные темы.'''
    class Meta:
        verbose_name = "план изучения (roadmap)"
        verbose_name_plural = 'планы изучения (roadmaps)'
    name = models.CharField(
        max_length=45, 
        verbose_name="Название",
        help_text="на русском")
    name_en = models.CharField(
        max_length=20, 
        verbose_name='Roadmap',
        help_text="на английском")
    description = models.TextField(
        verbose_name="Краткое описание:",
        help_text = "цели и задачи, сроки, основные темы")
        
    def __str__(self) -> str:
        return f"{self.name} ({self.name_en})"
    
    def get_courses(self):
        return Topik.objects.filter(roadmap=self).count()
    
    def get_subjects(self):
        count = 0
        for topik in Topik.objects.filter(roadmap=self):
            count += topik.get_subjects()
        return count
    
    def get_level(self):
        level = 0
        for topik in Topik.objects.filter(roadmap=self):
            level += topik.get_level()
        return level
    
    def get_keywords(self):
        count_keywords = 0
        for topik in Topik.objects.filter(roadmap=self):
            count_keywords += topik.get_keywords()
        return count_keywords

class Topik(models.Model):
    '''Отдельный курс: объемная тема обсуждения, изучения. основная тема из плана изучения. 
    Отражающая текущий уровень усвоения. Связана с подтемами, которые связаны с ресурсами, а так же ключевыми словами'''
    class Meta:
        verbose_name = "курс для изучения"
        verbose_name_plural = 'курсы для изучения'
    name = models.CharField(
        max_length=35, 
        verbose_name="название курса")
    name_en = models.CharField(
        max_length=20, 
        verbose_name='topik',
        help_text="название на английском")
    description = models.TextField(
        verbose_name="краткое описание",
        help_text="тезисное описание или цели курса")
    study_level = models.FloatField(
        verbose_name='уровень обучения',
        help_text="уровень обучения (для сортировки)",
        default=1
        # unique=True
        )
    roadmap = models.ForeignKey(
        RoadMapStudy, 
        verbose_name='план изучения (roadmap)',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.name_en})"
    
    def get_level(self):
        level = 0
        for subject in Subject.objects.filter(topik=self):
            level += subject.current_level
        return level
    
    def get_subjects(self):
        return Subject.objects.filter(topik=self).count()
    
    def get_keywords(self):
        count_keywords = 0
        for subject in Subject.objects.filter(topik=self):
            count_keywords += subject.get_keywords()
        return count_keywords
    
class Subject(models.Model):
    '''Выделенная тема для изучения'''
    class Meta:
        verbose_name = "Тема для изучения"
        verbose_name_plural = 'Темы для изучения'
    name = models.CharField(
        max_length=30, 
        verbose_name="название темы"
        )
    name_en = models.CharField(
        max_length=20, 
        verbose_name='subject',
        help_text="название на английском")
    current_level = models.SmallIntegerField(
        verbose_name='текущий уровень знаний', 
        default=0)
    description = models.TextField(
        verbose_name="цели и задачи темы",
        help_text="описать основные цели и задачи изучаемой темы")
    resource = models.ForeignKey(
        'ResourceStudy',
        verbose_name='ссылка на ресурс',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    keywords = models.ManyToManyField(
        'KeyWord',
        verbose_name="ключевые слова",
        blank=True,
        null=True
    )
    topik = models.ForeignKey(
        Topik,
        verbose_name='курс обучения',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    ) 
       
    def __str__(self) -> str:
        return f"{self.name} ({self.topik})"
    
    def get_keywords(self):
        return self.keywords.all().count()
    
#----------------------------------------------

class ResourceStudy(models.Model):
    '''ресурсы для самостоятельного ознакомления с темой. Ссылка на отличную статью, видео, главу книги более 
    глубоко раскрывающая тему. 
    TODO: продумать систему оценки качества и 
    актуальности статьи
    TODO: отлично будет если у курса есть API отражающий уровень 
    прохождения курса. И отображение этого уровня непосредственно в роадмап для зарегистрированного
    пользователя'''
    class Meta:
        verbose_name = "ссылка на ресурс по теме"
        verbose_name_plural = 'ссылки на ресурсы'
    name = models.CharField(
        max_length=30, 
        verbose_name="Название ресурса"
        )
    url = models.URLField(verbose_name="Ссылка на ресурс")
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    
class KeyWord(models.Model):
    '''Ключевые слова для данной темы или ресурса'''
    class Meta:
        verbose_name = "ключевое слово"
        verbose_name_plural = 'ключевые слова'
    word = models.CharField(
        max_length=35, 
        verbose_name="слово, словосочетание")
    word_en = models.CharField(
        max_length=20, 
        verbose_name='слово на английском')
    definition = models.TextField(verbose_name="строгое определение")
    
    
    def __str__(self) -> str:
        return f"{self.word} ({self.word_en})"
    

    
class FaQ(models.Model):
    '''Часто задаваемые вопросы по плану занятий, теме, ключевому слову'''
    class Meta:
        verbose_name = "часто задаваемый вопрос"
        verbose_name_plural = 'часто задаваемые вопросы'
    question = models.CharField(
        max_length=35, 
        verbose_name="кратко сформированный вопрос")
    answer = models.TextField(verbose_name="Развернутый ответ на вопрос")