from os import error
from django.conf import settings
from django.db import connection

class AvgMusic():

    def __init__(self):
        self.nameDB = self.specifyDB()

    def specifyDB(self):
        try:
            if 'postgresql' in settings.DATABASES['default']['ENGINE']:
                return 'psql'
            elif 'mysql' in settings.DATABASES['default']['ENGINE']:
                return 'mysql' 
        except :
            pass

    def createProcedure(self):
        with connection.cursor() as cursor:
            if self.nameDB == 'psql':
                cursor.execute(

                    '''
                    CREATE OR REPLACE PROCEDURE public.update_avg_music()
                    LANGUAGE plpgsql
                    AS $procedure$
                    declare
                        rec record;
                        begin
                            
                                for rec in
                                select avg(rate_r) as avg_rate ,music_r_id
                                
                                from public.profiles_rate 
                                group by music_r_id
                                
                            loop
                            
                            UPDATE public.general_music SET "avg_rate" = rec.avg_rate where "id" = rec.music_r_id ;
                            
                            end loop;
                                
                        END;
                    $procedure$
                    ;
                    '''
                    )


            elif self.nameDB == 'mysql':
                try:
                    cursor.execute(
                        '''
                        CREATE PROCEDURE update_avg_music()
                        BEGIN
                                UPDATE general_music join (
                                        select avg(rate_r) as avrage_rate ,music_r_id        
                                        from profiles_rate 
                                        group by music_r_id 
                                ) AS rec ON  id = rec.music_r_id SET avg_rate = rec.avrage_rate  ;                 
                        END                    
                        '''
                        )
                except :
                    pass


    @classmethod
    def callProcedure(self):
        with connection.cursor() as cursor:
            cursor.execute("call update_avg_music() ;")






